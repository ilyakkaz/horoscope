from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

prediction_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Получить", callback_data="pred_get_ru"),
                                             InlineKeyboardMarkup(text="Пригласить", callback_data="pred_share_ru")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Скрыть", callback_data="delete_msg")
                                         ]
                                     ])

prediction_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Receive", callback_data="pred_get_en"),
                                             InlineKeyboardMarkup(text="Invite", callback_data="pred_share_en")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="hide", callback_data="delete_msg")
                                         ]
                                     ])

prediction_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Recibir", callback_data="pred_get_es"),
                                             InlineKeyboardMarkup(text="Invitar", callback_data="pred_share_es")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="esconder", callback_data="delete_msg")
                                         ]
                                     ])

prediction_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Erhalten", callback_data="pred_get_de"),
                                             InlineKeyboardMarkup(text="Einladen", callback_data="pred_share_de")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="ausblenden", callback_data="delete_msg")
                                         ]
                                     ])

check_ru = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Проверить", callback_data="check_referrals")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="Назад", callback_data="Предсказание")
                                    ]
                                ])

check_en = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Check", callback_data="check_referrals")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="Back to", callback_data="Предсказание")
                                    ]
                                ])

check_es = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Cheque", callback_data="check_referrals")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="De regreso", callback_data="Предсказание")
                                    ]
                                ])


check_de = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Prüfen", callback_data="check_referrals")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="Schließen", callback_data="delete_msg")
                                    ]
                                ])


more_prediction_ru = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Еще предсказание", callback_data="pred_get_ru")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="Скрыть", callback_data="delete_msg")
                                    ]
                                ])


more_prediction_en = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Another prediction", callback_data="pred_get_ru")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                    ]
                                ])


more_prediction_es = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Otra predicción", callback_data="pred_get_ru")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                    ]
                                ])


more_prediction_de = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardMarkup(text="Noch eine Vorhersage", callback_data="pred_get_ru")
                                    ],
                                    [
                                        InlineKeyboardMarkup(text="Schließen", callback_data="delete_msg")
                                    ]
                                ])


delete_msg_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Скрыть", callback_data="delete_msg")
                                         ]
                                     ])

delete_msg_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])

delete_msg_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])

delete_msg_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Ausblenden", callback_data="delete_msg")
                                         ]
                                     ])
