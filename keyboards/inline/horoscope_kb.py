from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

horoscope_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Любовный", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Деловой", callback_data="h_business")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Общий", callback_data="h_all"),
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Love", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Business", callback_data="h_business")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                             InlineKeyboardMarkup(text="hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Amor", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Negocio", callback_data="h_business")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                             InlineKeyboardMarkup(text="esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Liebe", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Unternehmen", callback_data="h_business")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Allgemeines", callback_data="h_all"),
                                             InlineKeyboardMarkup(text="ausblenden", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love1_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_love5_1")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Деловой", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Общий", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])

horoscope_love2_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_love5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Деловой", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Общий", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love3_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_love5_1"),
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_love5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Деловой", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Общий", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love4_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_love5_2"),
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_love5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Деловой", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Общий", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love5_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_love5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Деловой", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Общий", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business1_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_business5_1"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Любовный", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Общий", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business2_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_business5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Любовный", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Общий", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business3_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_business5_1"),
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_business5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Любовный", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Общий", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business4_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_business5_2"),
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_business5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Любовный", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Общий", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business5_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_business5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Любовный", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Общий", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all1_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_all5_1"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Любовный", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Деловой", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all2_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_all"),
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_all5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Любовный", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Деловой", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all3_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_all5_1"),
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_all5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Любовный", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Деловой", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all4_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_all5_2"),
                                             InlineKeyboardMarkup(text="Вперед⏩", callback_data="h_all5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Любовный", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Деловой", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all5_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Назад", callback_data="h_all5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Любовный", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Деловой", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Назад", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love1_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_love5_1")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Business", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])

horoscope_love2_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_love5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Business", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love3_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_love5_1"),
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_love5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Business", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love4_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_love5_2"),
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_love5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Business", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love5_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_love5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Business", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business1_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_business5_1"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Love", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business2_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_business5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Love", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business3_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_business5_1"),
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_business5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Love", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business4_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_business5_2"),
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_business5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Love", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business5_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_business5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Love", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all1_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_all5_1"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Love", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Business", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all2_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_all"),
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_all5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Love", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Business", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all3_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_all5_1"),
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_all5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Love", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Business", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all4_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_all5_2"),
                                             InlineKeyboardMarkup(text="Next⏩", callback_data="h_all5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Love", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Business", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all5_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Previous", callback_data="h_all5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Love", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Business", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])

horoscope_love1_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_love5_1")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Negocio", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])

horoscope_love2_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_love5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Negocio", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love3_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_love5_1"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_love5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Negocio", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love4_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_love5_2"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_love5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Negocio", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love5_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_love5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Negocio", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business1_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_business5_1"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Amor", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business2_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_business5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Amor", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business3_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_business5_1"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_business5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Amor", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business4_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_business5_2"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_business5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Amor", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business5_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_business5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Amor", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="General", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all1_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_all5_1"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Amor", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Negocio", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all2_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_all"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_all5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Amor", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Negocio", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all3_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_all5_1"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_all5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Amor", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Negocio", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all4_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_all5_2"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_all5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Amor", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Negocio", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all5_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_all5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Amor", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Negocio", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love1_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_love5_1")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Unternehmen", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Allgemeines", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])

horoscope_love2_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_love5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Unternehmen", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Allgemeines", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love3_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_love5_1"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_love5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Unternehmen", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Allgemeines", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love4_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Anterior", callback_data="h_love5_2"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_love5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Unternehmen", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Allgemeines", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_love5_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Bisherige", callback_data="h_love5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Unternehmen", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Allgemeines", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business1_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="ferner⏩", callback_data="h_business5_1"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Liebe", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Allgemeines", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business2_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪ferner", callback_data="h_business"),
                                             InlineKeyboardMarkup(text="Siguiente⏩", callback_data="h_business5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Liebe", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Allgemeines", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business3_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Bisherige", callback_data="h_business5_1"),
                                             InlineKeyboardMarkup(text="ferner⏩", callback_data="h_business5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Liebe", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Allgemeines", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business4_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Bisherige", callback_data="h_business5_2"),
                                             InlineKeyboardMarkup(text="ferner⏩", callback_data="h_business5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Liebe", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Allgemeines", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_business5_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Bisherige", callback_data="h_business5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Liebe", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Allgemeines", callback_data="h_all"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all1_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="ferner⏩", callback_data="h_all5_1"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Liebe", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Unternehmen", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all2_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Bisherige", callback_data="h_all"),
                                             InlineKeyboardMarkup(text="ferner⏩", callback_data="h_all5_2"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Liebe", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Unternehmen", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all3_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Bisherige", callback_data="h_all5_1"),
                                             InlineKeyboardMarkup(text="ferner⏩", callback_data="h_all5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Liebe", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Unternehmen", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all4_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Bisherige", callback_data="h_all5_2"),
                                             InlineKeyboardMarkup(text="ferner⏩", callback_data="h_all5_4"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Liebe", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Unternehmen", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])


horoscope_all5_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="⏪Bisherige", callback_data="h_all5_3"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Liebe", callback_data="h_love"),
                                             InlineKeyboardMarkup(text="Unternehmen", callback_data="h_business"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="schließen", callback_data="delete_msg")
                                         ]
                                     ])