from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

notify_time_kb = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="00:00", callback_data="00:00"),
                                             InlineKeyboardMarkup(text="01:00", callback_data="01:00"),
                                             InlineKeyboardMarkup(text="02:00", callback_data="02:00"),
                                             InlineKeyboardMarkup(text="03:00", callback_data="03:00"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="04:00", callback_data="04:00"),
                                             InlineKeyboardMarkup(text="05:00", callback_data="05:00"),
                                             InlineKeyboardMarkup(text="06:00", callback_data="06:00"),
                                             InlineKeyboardMarkup(text="07:00", callback_data="07:00"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="08:00", callback_data="08:00"),
                                             InlineKeyboardMarkup(text="09:00", callback_data="09:00"),
                                             InlineKeyboardMarkup(text="10:00", callback_data="10:00"),
                                             InlineKeyboardMarkup(text="11:00", callback_data="11:00"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="12:00", callback_data="12:00"),
                                             InlineKeyboardMarkup(text="13:00", callback_data="13:00"),
                                             InlineKeyboardMarkup(text="14:00", callback_data="14:00"),
                                             InlineKeyboardMarkup(text="15:00", callback_data="15:00"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="16:00", callback_data="16:00"),
                                             InlineKeyboardMarkup(text="17:00", callback_data="17:00"),
                                             InlineKeyboardMarkup(text="18:00", callback_data="18:00"),
                                             InlineKeyboardMarkup(text="19:00", callback_data="19:00"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="20:00", callback_data="20:00"),
                                             InlineKeyboardMarkup(text="21:00", callback_data="21:00"),
                                             InlineKeyboardMarkup(text="22:00", callback_data="22:00"),
                                             InlineKeyboardMarkup(text="23:00", callback_data="23:00"),
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="❌", callback_data="delete_msg")
                                         ]
                                     ])


edit_notify_time_kb_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Изменить время", callback_data="edit_time"),
                                             InlineKeyboardMarkup(text="часовой пояс", callback_data="edit_time_zone")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Изменить гороскопы", callback_data="select_horo"),
                                             InlineKeyboardMarkup(text="Скрыть", callback_data="delete_msg")
                                         ]
                                     ])


edit_notify_time_kb_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Change time", callback_data="edit_time"),
                                             InlineKeyboardMarkup(text="Timezone", callback_data="edit_time_zone")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Change horoscopes", callback_data="select_horo"),
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


edit_notify_time_kb_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Cambio de hora", callback_data="edit_time"),
                                             InlineKeyboardMarkup(text="Zona horaria", callback_data="edit_time_zone")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Cambiar horóscopos", callback_data="select_horo"),
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


edit_notify_time_kb_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Zeit ändern", callback_data="edit_time"),
                                             InlineKeyboardMarkup(text="Zeitzone", callback_data="edit_time_zone")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Horoskope ändern", callback_data="select_horo"),
                                             InlineKeyboardMarkup(text="Ausblenden", callback_data="delete_msg")
                                         ]
                                     ])

on_off_ru = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="Вкл\выкл любовный", callback_data="on_off_love"),
                                             InlineKeyboardMarkup(text="Вкл\выкл деловой", callback_data="on_off_business")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="Вкл\выкл общий", callback_data="on_off_regular"),
                                             InlineKeyboardMarkup(text="Скрыть", callback_data="delete_msg")
                                         ]
                                     ])


on_off_en = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="On/off love", callback_data="on_off_love"),
                                             InlineKeyboardMarkup(text="On/off business", callback_data="on_off_business")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="On/off general", callback_data="on_off_regular"),
                                             InlineKeyboardMarkup(text="Hide", callback_data="delete_msg")
                                         ]
                                     ])


on_off_es = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="On/off Amor", callback_data="on_off_love"),
                                             InlineKeyboardMarkup(text="On/off Negocio", callback_data="on_off_business")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="On/off general", callback_data="on_off_regular"),
                                             InlineKeyboardMarkup(text="Esconder", callback_data="delete_msg")
                                         ]
                                     ])


on_off_de = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             InlineKeyboardMarkup(text="On/off Liebe", callback_data="on_off_love"),
                                             InlineKeyboardMarkup(text="On/off Geschäft", callback_data="on_off_business")
                                         ],
                                         [
                                             InlineKeyboardMarkup(text="On/off Allgemein", callback_data="on_off_regular"),
                                             InlineKeyboardMarkup(text="Ausblenden", callback_data="delete_msg")
                                         ]
                                     ])