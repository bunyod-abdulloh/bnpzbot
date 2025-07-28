from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.admin_db import AdminDB
from utils.db_api.postgres import Database
from utils.db_api.user_db import UserDB

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()
udb = UserDB(db)
admdb = AdminDB(db)
