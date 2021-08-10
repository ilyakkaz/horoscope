from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language_kb = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardMarkup(text="🇷🇺RU", callback_data="ru"),
                                           InlineKeyboardMarkup(text="🇺🇸EN", callback_data="en")
                                       ],
                                       [
                                           InlineKeyboardMarkup(text="🇪🇸ES", callback_data="es"),
                                           InlineKeyboardMarkup(text="🇩🇪DE", callback_data="de")
                                       ]
                                   ])

time_zone_kb = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardMarkup(text="UTC-1 (Cape Verde)", callback_data="UTC-1"),
                                            InlineKeyboardMarkup(text="UTC-2 (South Georgia)", callback_data="UTC-2"),
                                        ],
                                        [
                                            InlineKeyboardMarkup(text="UTC-3 (Argentina)", callback_data="UTC-3"),
                                            InlineKeyboardMarkup(text="UTC-4 (Virgin Islands)", callback_data="UTC-4"),

                                        ],
                                        [
                                            InlineKeyboardMarkup(text="UTC-5 (Haiti)", callback_data="UTC-5"),
                                            InlineKeyboardMarkup(text="UTC-6 (Honduras)", callback_data="UTC-6")
                                        ],
                                        [
                                            InlineKeyboardMarkup(text="UTC-7 (Arizona)", callback_data="UTC-7"),
                                            InlineKeyboardMarkup(text="UTC-8 (California)", callback_data="UTC-8"),
                                        ],
                                        [
                                            InlineKeyboardMarkup(text="UTC-9 (Alaska)", callback_data="UTC-9"),
                                            InlineKeyboardMarkup(text="UTC-10 (Hawaii)", callback_data="UTC-10"),
                                        ],
                                        [
                                            InlineKeyboardMarkup(text="UTC(0)", callback_data="UTC-0"),
                                            InlineKeyboardMarkup(text="UTC+1 (Algeria)", callback_data="UTC+1")
                                        ],
                                        [
                                            InlineKeyboardMarkup(text="UTC+2 (Brussels)", callback_data="UTC+2"),
                                            InlineKeyboardMarkup(text="UTC+3 (Москва)", callback_data="UTC+3"),
                                        ],
                                        [
                                            InlineKeyboardMarkup(text="UTC+4 (Саратов)", callback_data="UTC+4"),
                                            InlineKeyboardMarkup(text="UTC+5 (Челябинск)", callback_data="UTC+5"),
                                        ],
                                        [
                                            InlineKeyboardMarkup(text="UTC+6 (Омск)", callback_data="UTC+6"),
                                            InlineKeyboardMarkup(text="UTC+7 (Новосибирск)", callback_data="UTC+7")
                                        ],
                                        [
                                            InlineKeyboardMarkup(text="UTC+8 (Иркутск)", callback_data="UTC+8"),
                                            InlineKeyboardMarkup(text="UTC+9 (Якутск)", callback_data="UTC+9"),
                                        ],
                                        [
                                            InlineKeyboardMarkup(text="UTC+10 (Хабаровск)", callback_data="UTC+10"),
                                            InlineKeyboardMarkup(text="UTC+11 (Сахалин)", callback_data="UTC+11")
                                        ],
                                        [
                                            InlineKeyboardMarkup(text="UTC+12 (Чукотка)", callback_data="UTC+12")
                                        ]
                                    ])


gender_kb_ru = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardMarkup(text="Мужчина", callback_data="Male"),
                                           InlineKeyboardMarkup(text="Женщина", callback_data="Female")
                                       ]
                                   ])


gender_kb_de = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardMarkup(text="Mann", callback_data="Male"),
                                           InlineKeyboardMarkup(text="Weiblich", callback_data="Female"),

                                       ]
                                   ])


gender_kb_es = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardMarkup(text="Hombre", callback_data="Male"),
                                           InlineKeyboardMarkup(text="Mujer", callback_data="Female"),

                                       ]
                                   ])


gender_kb_en = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardMarkup(text="Male", callback_data="Male"),
                                           InlineKeyboardMarkup(text="Female", callback_data="Female"),

                                       ]
                                   ])


skip_time_ru = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardMarkup(text="Пропустить", callback_data="skip_time_register")
                                       ]
                                   ])


skip_time_de = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardMarkup(text="Überspringen", callback_data="skip_time_register")
                                       ]
                                   ])


skip_time_es = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardMarkup(text="Saltar", callback_data="skip_time_register")
                                       ]
                                   ])


skip_time_en = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardMarkup(text="Skip", callback_data="skip_time_register")
                                       ]
                                   ])