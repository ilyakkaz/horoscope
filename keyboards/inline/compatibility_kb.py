from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

compatibility_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="По дате", callback_data="compatibility_date"),
                                             InlineKeyboardMarkup(text="По имени", callback_data="compatibility_name")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Скрыть", callback_data="delete_msg")
                                         ]
                                     ])


compatibility_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="By date", callback_data="compatibility_date"),
                                             InlineKeyboardMarkup(text="By the name", callback_data="compatibility_name")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


compatibility_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Por fecha", callback_data="compatibility_date"),
                                             InlineKeyboardMarkup(text="Por el nombre", callback_data="compatibility_name")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


compatibility_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Nach Datum", callback_data="compatibility_date"),
                                             InlineKeyboardMarkup(text="Anhand des Namens", callback_data="compatibility_name")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Ausblenden", callback_data="delete_msg")
                                         ]
                                     ])


back_compatibility_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="compatibility_call_back")
                                         ]
                                     ])

back_compatibility_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Back to", callback_data="compatibility_call_back")
                                         ]
                                     ])

back_compatibility_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="De regreso", callback_data="compatibility_call_back")
                                         ]
                                     ])

back_compatibility_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="zurück", callback_data="compatibility_call_back")
                                         ]
                                     ])

comp_ru = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Проверить", callback_data="check_referrals")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="Назад", callback_data="compatibility_call_back")
                                    ]
                                ])

comp_en = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Check", callback_data="check_referrals")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="Back to", callback_data="compatibility_call_back")
                                    ]
                                ])

comp_es = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Cheque", callback_data="check_referrals")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="De regreso", callback_data="compatibility_call_back")
                                    ]
                                ])

comp_de = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Prüfen", callback_data="check_referrals")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="zurück", callback_data="compatibility_call_back")
                                    ]
                                ])