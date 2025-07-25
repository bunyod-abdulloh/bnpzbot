from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminStates(StatesGroup):
    SEND_MEDIA_TO_USERS = State()
    SEND_TO_USERS = State()
