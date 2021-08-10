from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


SU_to_main_kb = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Главное меню",
                                                                  callback_data="SU")
                                         ]
                                     ])


SU_via_age_kb = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Родились после XXXX года",
                                                                  callback_data="after_age")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Родились до XXXX года",
                                                                  callback_data="before_age")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Родились в XXXX год",
                                                                  callback_data="select_age")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="🔴Отмена",
                                                                  callback_data="SU")
                                         ]
                                     ])


SU_accept_send_kb = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="✅Отправить",
                                                                  callback_data="su_send_msg_accept")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="🔴Отмена",
                                                                  callback_data="SU")
                                         ]
                                     ])


main_SU_kb = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Скачать таблицу всех юзеров", callback_data="excel_all")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Посмотреть статистику",
                                                                  callback_data="stat")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Отправить сообщение",
                                                                  callback_data="su_send_msg")
                                         ]
                                     ])


select_users_SU_kb = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="По языку", callback_data="SU_msg_language")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="По возрасту",
                                                                  callback_data="SU_msg_age")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="По дате (число, месяц)",
                                                                  callback_data="SU_msg_date")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Главное меню",
                                                                  callback_data="SU")
                                         ]
                                     ])


SU_msg_language_kb = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="🇷🇺 👨‍👦‍👦Всем", callback_data="SU_msg_ru_all"),
                                             InlineKeyboardMarkup(text="🇷🇺 🙍‍♀️Ж", callback_data="SU_msg_ru_female"),
                                             InlineKeyboardMarkup(text="🇷🇺 🙍‍♂️М", callback_data="SU_msg_ru_male")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="🇺🇸 👨‍👦‍👦Всем", callback_data="SU_msg_en_all"),
                                             InlineKeyboardMarkup(text="🇺🇸 🙍‍♀️Ж", callback_data="SU_msg_en_female"),
                                             InlineKeyboardMarkup(text="🇺🇸 🙍‍♂️М", callback_data="SU_msg_en_male")
                                         ],
                                         [
                                              InlineKeyboardMarkup(text="🇪🇸 👨‍👦‍👦Всем", callback_data="SU_msg_es_all"),
                                              InlineKeyboardMarkup(text="🇪🇸 🙍‍♀️Ж", callback_data="SU_msg_es_female"),
                                              InlineKeyboardMarkup(text="🇪🇸 🙍‍♂️М", callback_data="SU_msg_es_male")
                                         ],
                                         [
                                              InlineKeyboardMarkup(text="🇩🇪 👨‍👦‍👦Всем", callback_data="SU_msg_de_all"),
                                              InlineKeyboardMarkup(text="🇩🇪 🙍‍♀️Ж", callback_data="SU_msg_de_female"),
                                              InlineKeyboardMarkup(text="🇩🇪 🙍‍♂️М", callback_data="SU_msg_de_male")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Главное меню",
                                                                  callback_data="SU")
                                         ]
                                     ])