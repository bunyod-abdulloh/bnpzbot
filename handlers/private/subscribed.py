from aiogram import types
from magic_filter import F

from data.config import CHANNELS
from handlers.private.start import generate_invite_button
from loader import bot, dp


async def not_subcribe_message(call: types.CallbackQuery):
    await call.answer(
        text=f"Ikkala kanalga ham a'zo bo'lishingiz lozim!", show_alert=True
    )


@dp.callback_query_handler(F.data == "subscribed")
async def subscribe_callback(call: types.CallbackQuery):
    first_channel = (await bot.get_chat_member(chat_id=CHANNELS[0], user_id=call.from_user.id)).status
    second_channel = (await bot.get_chat_member(chat_id=CHANNELS[1], user_id=call.from_user.id)).status

    if first_channel == 'left' or second_channel == 'left':
        await not_subcribe_message(call=call)
    elif first_channel == 'kicked' or second_channel == 'kicked':
        await not_subcribe_message(call=call)
    else:
        await call.message.edit_text(
            text=f"So'nggi qadam!\n\nBepul online dars kursiga qo'shilish uchun 5 ta do'stingizni taklif qiling.\n\n"
                 f"Takliflar soni 5 ta bo'lganida Siz yopiq kanalga havola(link) olasiz.",
            reply_markup=await generate_invite_button(call.from_user.id)
        )
