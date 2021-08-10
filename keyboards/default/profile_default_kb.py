from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


profile_ru = ReplyKeyboardMarkup(keyboard=[
                                     [
                                         KeyboardButton(text="Настройки"),
                                         KeyboardButton(text="Уведомления")
                                     ],
                                     [
                                         KeyboardButton(text="Назад")
                                     ]
                                 ],
                                 resize_keyboard=True)

profile_en = ReplyKeyboardMarkup(keyboard=[
                                      [
                                          KeyboardButton(text="Settings"),
                                          KeyboardButton(text="Notifications")
                                      ],
                                      [
                                          KeyboardButton(text="Back to")
                                      ]
                                  ],
                                 resize_keyboard=True)

profile_es = ReplyKeyboardMarkup(keyboard=[
                                      [
                                          KeyboardButton(text="Ajustes"),
                                          KeyboardButton(text="Notificaciones")
                                      ],
                                      [
                                          KeyboardButton(text="De regreso")
                                      ]
                                  ],
                                 resize_keyboard=True)

profile_de = ReplyKeyboardMarkup(keyboard=[
                                      [
                                          KeyboardButton(text="die Einstellungen"),
                                          KeyboardButton(text="Benachrichtigungen")
                                      ],
                                      [
                                          KeyboardButton(text="zurück")
                                      ]
                                  ],
                                 resize_keyboard=True)

settings_profile_ru = ReplyKeyboardMarkup(keyboard=[
                                               [
                                                   KeyboardButton(text="Изменить язык")
                                               ],
                                               [
                                                   KeyboardButton(text="Изменить дату и время рождения")
                                               ],
                                               [
                                                   KeyboardButton(text="Назад")
                                               ]
                                           ],
                                 resize_keyboard=True)

settings_profile_en = ReplyKeyboardMarkup(keyboard=[
                                               [
                                                   KeyboardButton(text="Change the language")
                                               ],
                                               [
                                                   KeyboardButton(text="Change date and time of birth")
                                               ],
                                               [
                                                   KeyboardButton(text="Back to")
                                               ]
                                           ],
                                 resize_keyboard=True)

settings_profile_es = ReplyKeyboardMarkup(keyboard=[
                                               [
                                                   KeyboardButton(text="Cambia el idioma")
                                               ],
                                               [
                                                   KeyboardButton(text="Cambiar fecha y hora de nacimiento")
                                               ],
                                               [
                                                   KeyboardButton(text="De regreso")
                                               ]
                                           ],
                                 resize_keyboard=True)

settings_profile_de = ReplyKeyboardMarkup(keyboard=[
                                               [
                                                   KeyboardButton(text="Ändere die Sprache")
                                               ],
                                               [
                                                   KeyboardButton(text="Geburtsdatum und -uhrzeit ändern")
                                               ],
                                               [
                                                   KeyboardButton(text="zurück")
                                               ]
                                           ],
                                 resize_keyboard=True)
