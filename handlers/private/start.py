from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from keyboards.default.user import sign_up_dkb
from loader import dp, udb


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await udb.add_user(telegram_id=message.from_user.id)
    await message.answer(
        text="BNPZ botimizga xush kelibsiz!", reply_markup=sign_up_dkb()
    )

#
# @dp.message_handler(state="*", content_types=types.ContentType.ANY)
# async def handle_photo_id(message: types.Message):
#     print("sa")
#     await message.answer(
#         text=f"<code>{message.photo[-1].file_id}</code>"
#     )
