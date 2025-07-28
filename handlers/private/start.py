from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from loader import dp, udb


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await udb.add_user(telegram_id=message.from_user.id)
    await message.answer(
        text="BNPZ botimizga xush kelibsiz!"
    )
