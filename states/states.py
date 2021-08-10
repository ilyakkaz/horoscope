from aiogram.dispatcher.filters.state import StatesGroup, State


class SU(StatesGroup):
    msg_via_language = State()
    msg_via_age = State()
    msg_select_age = State()
    msg_text_age = State()
    msg_via_date = State()
    msg_select_date = State()
    msg_text_date = State()


class Pifagor(StatesGroup):
    date = State()


class Register(StatesGroup):
    birthday = State()
    time = State()


class Compatibility(StatesGroup):
    birthday = State()
    name = State()


class Settings(StatesGroup):
    language = State()
    birthday = State()
    time = State()


class Test(StatesGroup):
    date = State()


class Profile(StatesGroup):
    time_zone = State()