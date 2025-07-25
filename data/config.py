from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
CHANNELS = env.list("CHANNELS")
PRIVATE_CHANNEL = env.int("PRIVATE_CHANNEL")
ADMIN_GROUP = env.str("ADMIN_GROUP")
IP = env.str("IP")

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
