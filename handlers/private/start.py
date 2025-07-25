import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.deep_linking import get_start_link

from data.config import CHANNELS, PRIVATE_CHANNEL
from loader import dp, db, bot


async def generate_invite_button(user_id):
    link = await get_start_link(str(user_id))
    send_link_text = (
        f"Bepul online dars kursiga qo'shilish uchun quyidagi havola orqali botga a'zo bo'ling\n\n{link}"
    )
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Yuborish", switch_inline_query=send_link_text))
    return markup


async def send_welcome_message(message: types.Message):
    first_channel = await bot.get_chat(CHANNELS[0])
    second_channel = await bot.get_chat(CHANNELS[1])

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text=first_channel.full_name, url=f"https://t.me/{first_channel.username}"),
        types.InlineKeyboardButton(text=second_channel.full_name, url=f"https://t.me/{second_channel.username}"),
        types.InlineKeyboardButton(text="✅ A'zo bo'ldim!", callback_data="subscribed")
    )
    await message.answer(
        "Tabriklaymiz!!! Siz birinchi qadamni bosdingiz! Davom etish uchun quyidagi kanallarimizga a'zo bo'ling.\n\n"
        "Keyin \"✅ А'zo bo'ldim!\" tugmasini bosing",
        reply_markup=markup
    )


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user_id = message.from_user.id
    args = message.get_args()
    try:
        await db.add_user(telegram_id=message.from_user.id)
    except asyncpg.exceptions.UniqueViolationError:
        pass

    if args:
        inviter_id = int(args)
        invite_count = await db.count_members(inviter=inviter_id)

        if invite_count == 4:
            invite_link = (await bot.create_chat_invite_link(chat_id=PRIVATE_CHANNEL, member_limit=1)).invite_link
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Kanalga qo'shilish", url=invite_link))
            await bot.send_message(
                chat_id=inviter_id,
                text="Tabriklaymiz! Siz ushbu sovg'ani olishga haqli deb topildingiz.\n\n"
                     "Quyidagi tugma orqali yopiq kanalga qo'shiling.",
                reply_markup=markup, protect_content=True
            )
            await send_welcome_message(message)
        elif invite_count > 4:
            await send_welcome_message(message)
        else:
            try:
                await db.add_members(inviter=inviter_id, new_member=user_id, invite_count=1)
                inviter_name = (await bot.get_chat(chat_id=inviter_id)).full_name
                await bot.send_message(
                    chat_id=inviter_id,
                    text=(
                        f"Tabriklaymiz, {inviter_name}! Do’stingiz {message.from_user.full_name} "
                        f"Sizning unikal taklif havolangiz orqali botimizga qo’shildi.\n\n"
                        f"Bepul online dars kursiga qo'shilish uchun yana {4 - invite_count} ta do’stingizni "
                        f"taklif qiling."
                    ),
                    reply_markup=await generate_invite_button(user_id=inviter_id)
                )
                await send_welcome_message(message)
            except asyncpg.exceptions.UniqueViolationError:
                await message.answer("Siz bot uchun ro'yxatdan o'tgansiz!")
                await bot.send_message(
                    chat_id=inviter_id,
                    text=(
                        f"Foydalanuvchi {message.from_user.full_name} bot uchun avval ro'yxatdan o'tgan!\n\n"
                        "Iltimos, boshqa foydalanuvchi taklif qiling!"
                    )
                )
    else:
        await send_welcome_message(message)
