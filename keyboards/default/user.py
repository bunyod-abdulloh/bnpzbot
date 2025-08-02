from aiogram.types import ReplyKeyboardMarkup


def sign_up_dkb():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("Ro'yxatdan o'tish")
    return btn
