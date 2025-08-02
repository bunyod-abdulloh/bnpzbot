from aiogram.dispatcher.filters.state import StatesGroup, State


class UserGetDatas(StatesGroup):
    FULLNAME = State()
    POSITION = State()
    ADDRESS = State()
    INVERTOR = State()
    PANEL = State()
    PHOTO_ONE = State()
    PHOTO_TWO = State()
    PHOTO_THREE = State()
    PANELS_COUNT = State()
