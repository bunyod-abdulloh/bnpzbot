import logging

from aiogram import Dispatcher

from data.config import ADMIN_GROUP


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMIN_GROUP, "Bot ishga tushdi")

    except Exception as err:
        logging.exception(err)
