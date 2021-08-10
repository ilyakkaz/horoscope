import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from keyboards.default.main_kb import menu_ru, menu_en, menu_de, menu_es
from states.states import Register
from utils.db_api import quick_commands as qc
from keyboards.inline.start_kb import language_kb, time_zone_kb, gender_kb_ru, gender_kb_de, gender_kb_es, gender_kb_en, \
    skip_time_de, skip_time_es, skip_time_en, skip_time_ru
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    # try:
    user = await qc.get_user(id=int(message.from_user.id))
    print(user)
    if not user:
        referral = message.get_args()
        print(referral)
        id = message.from_user.id
        fullname = message.from_user.full_name
        username = message.from_user.username
        language = None
        time_zone = None
        birthday = None
        time_birthday = None
        sex = None
        notify_time = None
        if not referral:
            referral = 0
        await qc.add_user(id=id, fullname=fullname, username=username, language=language, time_zone=time_zone,
                          birthday=birthday, time_birthday=time_birthday, sex=sex, referral=int(referral), notify_time=notify_time, prediction=0)
        await message.answer(f"Выберите язык.\n"
                             f"\n"
                             f"Choose language.\n"
                             f"\n"
                             f"Elige lengua.\n"
                             f"\n"
                             f"Sprache wählen.", reply_markup=language_kb)
    else:
        user = await qc.get_user(id=int(message.from_user.id))
        if user.language == "ru" and user.sex in ("Male", "Female"):
            await message.answer(f"Чтобы пользоваться ботом, используйте кнопки", reply_markup=menu_ru)
        elif user.language == "en" and user.sex in ("Male", "Female"):
            await message.answer(f"To use the bot, use the buttons", reply_markup=menu_en)
        elif user.language == "es" and user.sex in ("Male", "Female"):
            await message.answer(f"Para usar el bot, use los botones", reply_markup=menu_es)
        elif user.language == "de" and user.sex in ("Male", "Female"):
            await message.answer(f"Um den Bot zu verwenden, verwenden Sie die Schaltflächen\n",
                                 reply_markup=menu_de)
        else:
            await message.answer(f"Выберите язык.\n"
                                 f"\n"
                                 f"Choose language.\n"
                                 f"\n"
                                 f"Elige lengua.\n"
                                 f"\n"
                                 f"Sprache wählen.", reply_markup=language_kb)
    await state.finish()


# except:
#     await message.answer(f"ERROR")
#     pass


@dp.callback_query_handler(Text(equals=["ru", "en", "es", "de"]))
async def language(call: types.CallbackQuery):
    language = call.data
    if language == "ru":
        await call.message.edit_text(f"Выберите часовой пояс", reply_markup=time_zone_kb)
    if language == "en":
        await call.message.edit_text(f"Select your time zone", reply_markup=time_zone_kb)
    if language == "es":
        await call.message.edit_text(f"Seleccione su zona horaria", reply_markup=time_zone_kb)
    if language == "de":
        await call.message.edit_text(f"Wählen Sie Ihre Zeitzone", reply_markup=time_zone_kb)
    await qc.update_language(id=int(call.from_user.id), language=language)


@dp.callback_query_handler(Text(equals=["UTC-10", "UTC-9", "UTC-8", "UTC-7", "UTC-6", "UTC-5", "UTC-4", "UTC-3", "UTC-2", "UTC-1", "UTC-0", "UTC+12", "UTC+11", "UTC+10", "UTC+9",
                                        "UTC+8", "UTC+7", "UTC+6", "UTC+5", "UTC+4", "UTC+3", "UTC+2", "UTC+1"]))
async def time_zone(call: types.CallbackQuery):
    time_zone = call.data
    user = await qc.get_user(id=int(call.from_user.id))
    if user.language == "ru":
        await call.message.edit_text(f"Введите дату вашего рождения\n"
                                     f"<i>Например 21.04.1990</i>", reply_markup=None)
    if user.language == "en":
        await call.message.edit_text(f"Enter your date of birth\n"
                                     f"<i>For example 21/04/1990</i>", reply_markup=None)
    if user.language == "es":
        await call.message.edit_text(f"Introduzca su fecha de nacimiento\n"
                                     f"<i>Por ejemplo 21/04/1990</i>", reply_markup=None)
    if user.language == "de":
        await call.message.edit_text(f"Gib dein Geburtsdatum ein\n"
                                     f"<i>Zum Beispiel 15.04.1990</i>", reply_markup=None)
    await qc.update_time_zone(id=int(call.from_user.id), time_zone=time_zone)
    await Register.birthday.set()


@dp.message_handler(state=Register.birthday)
async def birthday(message: types.Message, state: FSMContext):
    try:
        date = message.text
    except:
        user = await qc.get_user(id=int(message.from_user.id))
        if user.language == "ru":
            await message.answer(f"Вы неправильно указали дату вашего рождения, укажите ее в формате:\n"
                                 f"<b>дд.мм.гггг</b> или <b>дд,мм,гггг</b> или <b>дд/мм/гггг</b>", reply_markup=None)
        if user.language == "en":
            await message.answer(f"You have incorrectly indicated your date of birth, please enter it in the format:"
                                 f"<b>dd.mm.yyyy</b> or <b>dd,mm,yyyy</b> or <b>dd/mm/yyyy</b>", reply_markup=None)
        if user.language == "es":
            await message.answer(f"Ha indicado incorrectamente su fecha de nacimiento, introdúzcala en el formato:"
                                 f"<b>dd.mm.aaaa</b> o <b>dd,mm,aaaa</b> o <b>dd/mm/aaaa</b>", reply_markup=None)
        if user.language == "de":
            await message.answer(f"Sie haben Ihr Geburtsdatum falsch angegeben, bitte geben Sie es im Format ein:"
                                 f"<b>dd.mm.yyyy</b> oder <b>dd,mm,yyyy</b> oder <b>dd/mm/yyyy</b>", reply_markup=None)
    try:
        date = date.replace(",", " ")
    except:
        print("нет такого символа для замены")
    try:
        date = date.replace(".", " ")
    except:
        print("нет такого символа для замены")
    try:
        date = date.replace("/", " ")
    except:
        print("нет такого символа для замены")
    date_split = date.split()
    try:
        print(int(date_split[0]), int(date_split[1]), int(date_split[2]))
        if 0 >= int(date_split[0]) or 31 < int(date_split[0]) or 0 > int(date_split[1]) or 12 < int(date_split[1]) \
                or 1910 >= int(date_split[2]) or int(date_split[2]) > 2021:
            user = await qc.get_user(id=int(message.from_user.id))
            if user.language == "ru":
                await message.answer(f"Вы неправильно указали дату вашего рождения, укажите ее в формате:\n"
                                     f"<b>дд.мм.гггг</b> или <b>дд,мм,гггг</b> или <b>дд/мм/гггг</b>",
                                     reply_markup=None)
            if user.language == "en":
                await message.answer(
                    f"You have incorrectly indicated your date of birth, please enter it in the format:"
                    f"<b>dd.mm.yyyy</b> or <b>dd,mm,yyyy</b> or <b>dd/mm/yyyy</b>", reply_markup=None)
            if user.language == "es":
                await message.answer(f"Ha indicado incorrectamente su fecha de nacimiento, introdúzcala en el formato:"
                                     f"<b>dd.mm.aaaa</b> o <b>dd,mm,aaaa</b> o <b>dd/mm/aaaa</b>", reply_markup=None)
            if user.language == "de":
                await message.answer(f"Sie haben Ihr Geburtsdatum falsch angegeben, bitte geben Sie es im Format ein:"
                                     f"<b>dd.mm.yyyy</b> oder <b>dd,mm,yyyy</b> oder <b>dd/mm/yyyy</b>",
                                     reply_markup=None)
        else:
            if (int(date_split[0]) >= 21 and int(date_split[1]) == 1) or (int(date_split[0]) <= 19 and int(date_split[1]) == 2):
                zodiac = "Aquarius"
            if (int(date_split[0]) >= 20 and int(date_split[1]) == 2) or (int(date_split[0]) <= 20 and int(date_split[1]) == 3):
                zodiac = "Pisces"
            if (int(date_split[0]) >= 21 and int(date_split[1]) == 3) or (int(date_split[0]) <= 20 and int(date_split[1]) == 4):
                zodiac = "Aries"
            if (int(date_split[0]) >= 21 and int(date_split[1]) == 4) or (int(date_split[0]) <= 21 and int(date_split[1]) == 5):
                zodiac = "Taurus"
            if (int(date_split[0]) >= 22 and int(date_split[1]) == 5) or (int(date_split[0]) <= 21 and int(date_split[1]) == 6):
                zodiac = "Gemini"
            if (int(date_split[0]) >= 22 and int(date_split[1]) == 6) or (int(date_split[0]) <= 22 and int(date_split[1]) == 7):
                zodiac = "Cancer"
            if (int(date_split[0]) >= 23 and int(date_split[1]) == 7) or (int(date_split[0]) <= 21 and int(date_split[1]) == 8):
                zodiac = "Leo"
            if (int(date_split[0]) >= 22 and int(date_split[1]) == 8) or (int(date_split[0]) <= 23 and int(date_split[1]) == 9):
                zodiac = "Virgo"
            if (int(date_split[0]) >= 24 and int(date_split[1]) == 9) or (int(date_split[0]) <= 23 and int(date_split[1]) == 10):
                zodiac = "Libra"
            if (int(date_split[0]) >= 24 and int(date_split[1]) == 10) or (int(date_split[0]) <= 22 and int(date_split[1]) == 11):
                zodiac = "Scorpio"
            if (int(date_split[0]) >= 23 and int(date_split[1]) == 11) or (int(date_split[0]) <= 22 and int(date_split[1]) == 12):
                zodiac = "Sagittarius"
            if (int(date_split[0]) >= 23 and int(date_split[1]) == 12) or (int(date_split[0]) <= 20 and int(date_split[1]) == 1):
                zodiac = "Capricorn"
            await qc.update_zodiac(id=int(message.from_user.id), zodiac=zodiac)
            await qc.update_birthday(id=int(message.from_user.id), birthday=date, birthday_day=f"{date_split[0]}", birthday_month=f"{date_split[1]}", birthday_year=f"{date_split[2]}")
            user = await qc.get_user(id=int(message.from_user.id))
            if user.language == "ru":
                await message.answer(f"Укажите время, в которое вы родились.\n "
                                     f"Например 14:45 или 14 45\n"
                                     f"\n"
                                     f"Если вы не знаете - вы можете пропустить этот шаг", reply_markup=skip_time_ru)
            if user.language == "en":
                await message.answer(f"Please enter the time you were born. \n"
                                     f"For example 14:45 or 14 45\n"
                                     f"\n"
                                     f"If you don't know - you can skip this step", reply_markup=skip_time_en)
            if user.language == "es":
                await message.answer(f"Ingrese la hora en que nació. \n"
                                     f"Por ejemplo 14:45 o 14 45\n"
                                     f"\n"
                                     f"Si no lo sabe, puede omitir este paso", reply_markup=skip_time_es)
            if user.language == "de":
                await message.answer(f"Bitte geben Sie Ihre Geburtszeit ein. \n"
                                     f"Zum Beispiel 14:45 oder 14 45\n"
                                     f"\n"
                                     f"Wenn Sie es nicht wissen, können Sie diesen Schritt überspringen",
                                     reply_markup=skip_time_de)
            await Register.time.set()
    except:
        user = await qc.get_user(id=int(message.from_user.id))
        if user.language == "ru":
            await message.answer(f"Вы неправильно указали дату вашего рождения, укажите ее в формате:\n"
                                 f"<b>дд.мм.гггг</b> или <b>дд,мм,гггг</b> или <b>дд/мм/гггг</b>", reply_markup=None)
        if user.language == "en":
            await message.answer(f"You have incorrectly indicated your date of birth, please enter it in the format:"
                                 f"<b>dd.mm.yyyy</b> or <b>dd,mm,yyyy</b> or <b>dd/mm/yyyy</b>", reply_markup=None)
        if user.language == "es":
            await message.answer(f"Ha indicado incorrectamente su fecha de nacimiento, introdúzcala en el formato:"
                                 f"<b>dd.mm.aaaa</b> o <b>dd,mm,aaaa</b> o <b>dd/mm/aaaa</b>", reply_markup=None)
        if user.language == "de":
            await message.answer(f"Sie haben Ihr Geburtsdatum falsch angegeben, bitte geben Sie es im Format ein:"
                                 f"<b>dd.mm.yyyy</b> oder <b>dd,mm,yyyy</b> oder <b>dd/mm/yyyy</b>", reply_markup=None)


@dp.callback_query_handler(text="skip_time_register", state=Register.time)
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    await qc.update_time_birthday(id=int(call.from_user.id), time_birthday="-")
    user = await qc.get_user(id=int(call.from_user.id))
    if user.language == "ru":
        await call.message.edit_text(f"Выберите ваш пол", reply_markup=gender_kb_ru)
    if user.language == "en":
        await call.message.edit_text(f"Choose your gender", reply_markup=gender_kb_en)
    if user.language == "es":
        await call.message.edit_text(f"Elige tu género", reply_markup=gender_kb_es)
    if user.language == "de":
        await call.message.edit_text(f"Wählen Sie ihr Geschlecht", reply_markup=gender_kb_de)
    await state.finish()


@dp.message_handler(state=Register.time)
async def birthday(message: types.Message, state: FSMContext):
    try:
        date = message.text
    except:
        user = await qc.get_user(id=int(message.from_user.id))
        if user.language == "ru":
            await message.answer(f"Вы неправильно указали время вашего рождения, укажите его в формате:\n"
                                 f"ЧЧ:ММ или 14 45", reply_markup=None)
        if user.language == "en":
            await message.answer(f"You have incorrectly entered the time of your birth, enter it in the format: \n"
                                 f"HH: MM or 14 45", reply_markup=None)
        if user.language == "es":
            await message.answer(f"Ingresó incorrectamente la hora de su nacimiento, ingréselo en el formato: \n"
                                 f"HH: MM o 14 45", reply_markup=None)
        if user.language == "de":
            await message.answer(
                f"Sie haben Ihre Geburtszeit falsch eingegeben, bitte geben Sie diese im Format ein: \n"
                f"HH: MM oder 14 45", reply_markup=None)
    try:
        date = date.replace(":", " ")
    except:
        print("нет такого символа для замены")
    date_split = date.split()
    try:
        print(int(date_split[0]), int(date_split[1]))
        if 0 >= int(date_split[0]) or 23 < int(date_split[0]) or 0 > int(date_split[1]) or 49 < int(date_split[1]):
            user = await qc.get_user(id=int(message.from_user.id))
            if user.language == "ru":
                await message.answer(f"Вы неправильно указали время вашего рождения, укажите его в формате:\n"
                                     f"ЧЧ:ММили 14 45", reply_markup=None)
            if user.language == "en":
                await message.answer(f"You have incorrectly entered the time of your birth, enter it in the format: \n"
                                     f"HH: MM or 14 45", reply_markup=None)
            if user.language == "es":
                await message.answer(f"Ingresó incorrectamente la hora de su nacimiento, ingréselo en el formato: \n"
                                     f"HH: MM o 14 45", reply_markup=None)
            if user.language == "de":
                await message.answer(
                    f"Sie haben Ihre Geburtszeit falsch eingegeben, bitte geben Sie diese im Format ein: \n"
                    f"HH: MM oder 14 45", reply_markup=None)
        else:
            await qc.update_time_birthday(id=int(message.from_user.id), time_birthday=date)
            user = await qc.get_user(id=int(message.from_user.id))
            if user.language == "ru":
                await message.answer(f"Выберите ваш пол", reply_markup=gender_kb_ru)
            if user.language == "en":
                await message.answer(f"Choose your gender", reply_markup=gender_kb_en)
            if user.language == "es":
                await message.answer(f"Elige tu género", reply_markup=gender_kb_es)
            if user.language == "de":
                await message.answer(f"Wählen Sie ihr Geschlecht", reply_markup=gender_kb_de)
            await state.finish()
    except:
        user = await qc.get_user(id=int(message.from_user.id))
        if user.language == "ru":
            await message.answer(f"Вы неправильно указали время вашего рождения, укажите его в формате:\n"
                                 f"ЧЧ:ММ или 14 45", reply_markup=None)
        if user.language == "en":
            await message.answer(f"You have incorrectly entered the time of your birth, enter it in the format: \n"
                                 f"HH: MM or 14 45", reply_markup=None)
        if user.language == "es":
            await message.answer(f"Ingresó incorrectamente la hora de su nacimiento, ingréselo en el formato: \n"
                                 f"HH: MM o 14 45", reply_markup=None)
        if user.language == "de":
            await message.answer(
                f"Sie haben Ihre Geburtszeit falsch eingegeben, bitte geben Sie diese im Format ein: \n"
                f"HH: MM oder 14 45", reply_markup=None)


@dp.callback_query_handler(Text(equals=["Male", "Female", "Other"]))
async def sex(call: types.CallbackQuery):
    sex = call.data
    user = await qc.get_user(id=int(call.from_user.id))
    await call.message.delete_reply_markup()
    if user.language == "ru":
        await call.message.answer(f"Отлично, вы зарегистрировались.\n"
                                  f"Чтобы пользоваться ботом, используйте кнопки", reply_markup=menu_ru)
    if user.language == "en":
        await call.message.answer(f"Great, you are registered.\n"
                                  f"To use the bot, use the buttons", reply_markup=menu_en)
    if user.language == "es":
        await call.message.answer(f"Genial, estás registrado.\n"
                                  f"Para usar el bot, use los botones", reply_markup=menu_es)
    if user.language == "de":
        await call.message.answer(f"Super, Sie sind registriert.\n"
                                  f"Um den Bot zu verwenden, verwenden Sie die Schaltflächen\n", reply_markup=menu_de)
    rand_hour = random.randint(12, 22)
    print("rand_hour - ", rand_hour)
    notify_time = f"{rand_hour}:00"
    print("notify_time - ", notify_time)
    user = await qc.get_user(id=int(call.from_user.id))
    user_time_zone = user.time_zone
    if user_time_zone == "UTC-10":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) + 10
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC-9":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) + 9
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC-8":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) + 8
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC-7":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) + 7
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC-6":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) + 6
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC-5":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) + 5
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC-4":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) + 4
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC-3":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) + 3
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC-2":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) + 2
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC-1":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) + 1
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC-0":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) + 0
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+1":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 1
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+2":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 2
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+3":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 3
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp > 24:
            moscow_temp = moscow_temp - 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+4":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 4
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp < 0:
            moscow_temp = moscow_temp + 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+5":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 5
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp < 0:
            moscow_temp = moscow_temp + 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+6":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 6
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp < 0:
            moscow_temp = moscow_temp + 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+7":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 7
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp < 0:
            moscow_temp = moscow_temp + 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+8":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 8
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp < 0:
            moscow_temp = moscow_temp + 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+9":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 9
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp < 0:
            moscow_temp = moscow_temp + 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+10":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 10
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp < 0:
            moscow_temp = moscow_temp + 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+11":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 11
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp < 0:
            moscow_temp = moscow_temp + 24
        moscow_time = f"{moscow_temp}:00"
    if user_time_zone == "UTC+12":
        hours = notify_time.replace(":", " ")
        hours = hours.split()
        moscow_temp = int(hours[0]) - 12
        if moscow_temp == 24:
            moscow_time = "00:00"
        if moscow_temp < 0:
            moscow_temp = moscow_temp + 24
        moscow_time = f"{moscow_temp}:00"
    await qc.update_sex(id=int(call.from_user.id), sex=sex, notify_time="default", moscow_time=moscow_time, notify_horo="Общий, ")
