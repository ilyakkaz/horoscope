from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Гороскоп"),
            KeyboardButton(text="Предсказание")
        ],
        [
            KeyboardButton(text="Совместимость"),
            KeyboardButton(text="Квадрат пифагора"),
        ],
        [
            KeyboardButton(text="Профиль")
        ]

    ],
    resize_keyboard=True
)


menu_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Horoscope"),
            KeyboardButton(text="Prediction")
        ],
        [
            KeyboardButton(text="Compatibility"),
            KeyboardButton(text="Pythagoras square")
        ],
        [
            KeyboardButton(text="Profile")
        ]

    ],
    resize_keyboard=True
)


menu_es = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Horóscopo"),
            KeyboardButton(text="Predicción")
        ],
        [
            KeyboardButton(text="Compatibilidad"),
            KeyboardButton(text="Plaza de pitágoras")
        ],
        [
            KeyboardButton(text="Perfil")
        ]

    ],
    resize_keyboard=True
)


menu_de = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Horoskop"),
            KeyboardButton(text="Prognose")
        ],
        [
            KeyboardButton(text="Kompatibilität"),
            KeyboardButton(text="Pythagoras-Platz")
        ],
        [
            KeyboardButton(text="Profil")
        ]

    ],
    resize_keyboard=True
)