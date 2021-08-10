from datetime import datetime
from pathlib import Path
import pytz
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile, ContentTypes

from keyboards.inline.SU_kb import main_SU_kb, select_users_SU_kb, SU_msg_language_kb, SU_to_main_kb, SU_accept_send_kb, \
    SU_via_age_kb
from loader import dp, bot
from states.states import SU
from utils.db_api import quick_commands as qc
import xlsxwriter


@dp.message_handler(text="SU", state='*')
async def def_name(message: types.Message, state: FSMContext):
    if int(message.from_user.id) in (312241087, 1028997010):
        await message.answer(f"Добро пожаловать в панель администратора", reply_markup=main_SU_kb)
    else:
        await message.answer(f"У вас недостаточно прав для этой команды")
    await state.finish()


@dp.callback_query_handler(text="SU", state='*')
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    if int(call.from_user.id) in (312241087, 1028997010):
        await call.message.answer(f"Добро пожаловать в панель администратора", reply_markup=main_SU_kb)
    else:
        await call.message.answer(f"У вас недостаточно прав для этой команды")
    await state.finish()


@dp.callback_query_handler(text="su_send_msg")
async def def_mame(call: types.CallbackQuery):
    await call.message.edit_text(f"Каким пользователям отправить сообщение?\n"
                                 f"\n"
                                 f"Выберите фильтр", reply_markup=select_users_SU_kb)


@dp.callback_query_handler(text="excel_all")
async def def_mame(call: types.CallbackQuery):
    msg = await call.message.edit_text(f"Таблица генерируется. Это может занять некоторое время.\n"
                                       f"Пожалуйста, ожидайте")
    users = await qc.select_all_users()
    print(users)
    # workbook = xlsxwriter.Workbook('C:/Users/Cortana/Desktop/commercialbots/goroskop_backup/all_users.xlsx')
    dir_path = Path.cwd()
    document = Path(dir_path, "all_users.xlsx")
    workbook = xlsxwriter.Workbook(document)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'id юзера')
    worksheet.write(0, 1, 'Имя')
    worksheet.write(0, 2, 'Юзернейм')
    worksheet.write(0, 3, 'Язык')
    worksheet.write(0, 4, 'Часовой пояс')
    worksheet.write(0, 5, 'Дата рождения')
    worksheet.write(0, 6, 'Время рождения')
    worksheet.write(0, 7, 'Пол')
    worksheet.write(0, 8, 'Реферрал')
    worksheet.write(0, 9, 'Время оповещения')
    worksheet.write(0, 10, 'Знак зодиака')
    worksheet.write(0, 11, 'Время оповещения (UTC-0)')
    worksheet.write(0, 12, 'Печенек за сегодня')
    worksheet.write(0, 13, 'Какие гороскопы приходят')
    worksheet.write(0, 14, 'Зарегистрировался')
    worksheet.write(0, 14, 'Последнее обновление в бд')
    row = 1
    col = 0
    for user in users:
        worksheet.write(row, col, f"{user.id}")
        col += 1
        worksheet.write(row, col, f"{user.fullname}")
        col += 1
        worksheet.write(row, col, f"{user.username}")
        col += 1
        worksheet.write(row, col, f"{user.language}")
        col += 1
        worksheet.write(row, col, f"{user.time_zone}")
        col += 1
        worksheet.write(row, col, f"{user.birthday}")
        col += 1
        worksheet.write(row, col, f"{user.time_birthday}")
        col += 1
        worksheet.write(row, col, f"{user.sex}")
        col += 1
        worksheet.write(row, col, f"{user.referral}")
        col += 1
        worksheet.write(row, col, f"{user.notify_time}")
        col += 1
        worksheet.write(row, col, f"{user.zodiac}")
        col += 1
        worksheet.write(row, col, f"{user.moscow_time}")
        col += 1
        worksheet.write(row, col, f"{user.prediction}")
        col += 1
        worksheet.write(row, col, f"{user.notify_horo}")
        col += 1
        worksheet.write(row, col, f"{user.created_at}")
        col += 1
        worksheet.write(row, col, f"{user.updated_at}")
        row += 1
        col = 0
    workbook.close()
    now = datetime.now(pytz.timezone("europe/moscow"))
    date = now.strftime("%d.%m.%Y %H:%M:%S")
    await call.message.answer_document(
        # document=InputFile("C:/Users/Cortana/Desktop/commercialbots/goroskop_backup/all_users.xlsx"),
        document=InputFile(f"{document}"),
        caption=f"Таблица со всеми данными из БД на\n"
                f"{date} (UTC+3)")
    await msg.delete()
    await call.message.answer(f"Вы возвращены в панель администратора", reply_markup=main_SU_kb)


@dp.callback_query_handler(text="SU_msg_date")
async def def_mame(call: types.CallbackQuery):
    total_users = await qc.count_users()
    total_male = await qc.count_users_sex(sex="Male")
    total_female = await qc.count_users_sex(sex="Female")
    total_ru = await qc.count_users_language(language="ru")
    total_ru_m = await qc.count_users_sex_language(sex="Male", language="ru")
    total_ru_f = await qc.count_users_sex_language(sex="Female", language="ru")
    total_en = await qc.count_users_language(language="en")
    total_en_m = await qc.count_users_sex_language(sex="Male", language="en")
    total_en_f = await qc.count_users_sex_language(sex="Female", language="en")
    total_es = await qc.count_users_language(language="es")
    total_es_m = await qc.count_users_sex_language(sex="Male", language="es")
    total_es_f = await qc.count_users_sex_language(sex="Female", language="es")
    total_de = await qc.count_users_language(language="de")
    total_de_m = await qc.count_users_sex_language(sex="Male", language="de")
    total_de_f = await qc.count_users_sex_language(sex="Female", language="de")
    referrals = await qc.count_users_referrers()
    await call.message.edit_text(f"👩‍👦‍👦Всего пользователей: {total_users}\n"
                                 f"🙍‍♀️ Женщин: {total_female}\n"
                                 f"🙍‍♂️ Мужчин: {total_male}\n"
                                 f"\n"
                                 f"🇷🇺 Пользователей: {total_ru}\n"
                                 f"🇷🇺🙍‍♀️ Женщин: {total_ru_f}\n"
                                 f"🇷🇺🙍‍♂️ Мужчин: {total_ru_m}\n"
                                 f"\n"
                                 f"🇺🇸 Пользователей: {total_en}\n"
                                 f"🇺🇸🙍‍♀️ Женщин: {total_en_f}\n"
                                 f"🇺🇸🙍‍♂️ Мужчин: {total_en_m}\n"
                                 f"\n"
                                 f"🇪🇸 Пользователей: {total_es}\n"
                                 f"🇪🇸🙍‍♀️ Женщин: {total_es_f}\n"
                                 f"🇪🇸🙍‍♂️ Мужчин: {total_es_m}\n"
                                 f"\n"
                                 f"🇩🇪 Пользователей: {total_de}\n"
                                 f"🇩🇪🙍‍♀️ Женщин: {total_de_f}\n"
                                 f"🇩🇪🙍‍♂️ Мужчин: {total_de_m}\n", reply_markup=SU_msg_language_kb)
    await SU.msg_via_date.set()


@dp.callback_query_handler(Text(equals=["SU_msg_ru_all", "SU_msg_ru_female", "SU_msg_ru_male",
                                        "SU_msg_en_all", "SU_msg_en_female", "SU_msg_en_male",
                                        "SU_msg_es_all", "SU_msg_es_female", "SU_msg_es_male",
                                        "SU_msg_de_all", "SU_msg_de_female", "SU_msg_de_male"]), state=SU.msg_via_date)
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    type_people = call.data
    if type_people == "SU_msg_ru_all":
        people = await qc.get_users_language(language="ru")
        text = "с языком RU (и мужчинам и женщинам)"
        language = "ru"
        sex = "All"
    if type_people == "SU_msg_en_all":
        people = await qc.get_users_language(language="en")
        text = "с языком EN (и мужчинам и женщинам)"
        language = "en"
        sex = "All"
    if type_people == "SU_msg_es_all":
        people = await qc.get_users_language(language="es")
        text = "с языком ES (и мужчинам и женщинам)"
        language = "es"
        sex = "All"
    if type_people == "SU_msg_de_all":
        people = await qc.get_users_language(language="de")
        text = "с языком DE (и мужчинам и женщинам)"
        language = "de"
        sex = "All"
    if type_people == "SU_msg_ru_female":
        people = await qc.get_users_language_and_sex(language="ru", sex="Female")
        text = "с языком RU (только женщинам)"
        language = "ru"
        sex = "Female"
    if type_people == "SU_msg_en_female":
        people = await qc.get_users_language_and_sex(language="en", sex="Female")
        text = "с языком EN (только женщинам)"
        language = "en"
        sex = "Female"
    if type_people == "SU_msg_es_female":
        people = await qc.get_users_language_and_sex(language="es", sex="Female")
        text = "с языком ES (только женщинам)"
        language = "es"
        sex = "Female"
    if type_people == "SU_msg_de_female":
        people = await qc.get_users_language_and_sex(language="de", sex="Female")
        text = "с языком DE (только женщинам)"
        language = "de"
        sex = "Female"
    if type_people == "SU_msg_ru_male":
        people = await qc.get_users_language_and_sex(language="ru", sex="Male")
        text = "с языком RU (только мужчинам)"
        language = "ru"
        sex = "Male"
    if type_people == "SU_msg_en_male":
        people = await qc.get_users_language_and_sex(language="en", sex="Male")
        text = "с языком EN (только мужчинам)"
        language = "en"
        sex = "Male"
    if type_people == "SU_msg_es_male":
        people = await qc.get_users_language_and_sex(language="es", sex="Male")
        text = "с языком ES (только мужчинам)"
        language = "es"
        sex = "Male"
    if type_people == "SU_msg_de_male":
        people = await qc.get_users_language_and_sex(language="de", sex="Male")
        text = "с языком DE (только мужчинам)"
        language = "de"
        sex = "Male"
    x = 0
    for man in people:
        x += 1
    if x == 0:
        await call.message.edit_text(f"По заданным фильтрам людей нет.\n"
                                     f"Измените критерии поиска", reply_markup=SU_msg_language_kb)
    else:
        await call.message.edit_text(f"Вы собираетесь отправить сообщение людям {text}.\n"
                                     f"\n"
                                     f"Укажите дату рождения человека, например 16.10", reply_markup=SU_to_main_kb)
        await state.update_data(people=f" людям {text}", language=language, sex=sex)
        await SU.msg_select_date.set()


@dp.message_handler(state=SU.msg_select_date)
async def def_name(message: types.Message, state: FSMContext):
        date = message.text
        try:
            try:
                date = date.replace(".", " ")
            except:
                pass
            try:
                date = date.replace(",", " ")
            except:
                pass
            try:
                date = date.replace("/", " ")
            except:
                pass
            date = date.split()
            day = date[0]
            month = date[1]
            data = await state.get_data()
            language = data.get("language")
            people = data.get("people")
            sex = data.get("sex")
            if sex in ("Female", "Male"):
                users = await qc.get_users_language_and_date_and_sex(language=language, sex=sex, day=str(day), month=str(month))
            else:
                users = await qc.get_users_language_date_no_sex(language=language, day=str(day), month=str(month))
            qty = 0
            for user in users:
                qty += 1
            if qty == 0:
                await message.answer(f"🔴Людей {people}, которые родились {day}.{month} НЕТ\n"
                                      f"\n"
                                      f"Укажите другую дату или вернитесь в главное меню", reply_markup=SU_to_main_kb)
            else:
                await message.answer(f"Вы собираетесь отправить сообщение людям {people}, которые родились {day}.{month} (Таких людей {qty} шт)\n"
                                     f"\n"
                                     f"Напишите текст сообщения.\n"
                                     f"Если хотите отправить фото - прикрепите фотографию и в описание добавьте текст", reply_markup=SU_to_main_kb)
                await state.update_data(users=users, date=date, qty=qty)
                await SU.msg_text_date.set()
        except:
            await message.answer(f"Вы неправильно указали дату. Укажите ее в формате 16,10 или 16.10 или 16/10 или 16 10", reply_markup=SU_to_main_kb)


@dp.message_handler(content_types=ContentTypes.TEXT, state=SU.msg_text_date)
async def def_name(message: types.Message, state: FSMContext):
    msg = message.text
    data = await state.get_data()
    people = data.get("people")
    type_age = data.get("type_age")
    year = data.get("year")
    qty = data.get("qty")
    sex = data.get("sex")
    language = data.get("language")
    date = data.get("date")
    if sex == "Female":
        await message.answer(f"Вы собираетесь отправить сообщение {qty} женщинам с языком {language}, которые родились {date[0]}.{date[1]}\n"
                                 f"\n"
                                 f"Оно будет выглядеть так:", reply_markup=SU_to_main_kb)
    if sex == "Male":
        await message.answer(f"Вы собираетесь отправить сообщение {qty} мужчинам с языком {language}, которые родились {date[0]}.{date[1]}\n"
                                 f"\n"
                                 f"Оно будет выглядеть так:", reply_markup=SU_to_main_kb)
    await message.answer(f"{msg}")
    await message.answer(f"Отправить?", reply_markup=SU_accept_send_kb)
    await state.update_data(photo_or_text="text", msg=msg)


@dp.message_handler(content_types=ContentTypes.PHOTO, state=SU.msg_text_date)
async def def_name(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    msg = message.caption
    data = await state.get_data()
    sex = data.get("sex")
    language = data.get("language")
    qty = data.get("qty")
    date = data.get("date")
    if sex == "Female":
        await message.answer(f"Вы собираетесь отправить сообщение {qty} женщинам с языком {language}, которые родились {date[0]}.{date[1]}\n"
                                 f"\n"
                                 f"Оно будет выглядеть так:", reply_markup=SU_to_main_kb)
    if sex == "Male":
        await message.answer(f"Вы собираетесь отправить сообщение {qty} мужчинам с языком {language}, которые родились {date[0]}.{date[1]}\n"
                                 f"\n"
                                 f"Оно будет выглядеть так:", reply_markup=SU_to_main_kb)
    if msg is None:
        await message.answer_photo(photo=photo)
    else:
        await message.answer_photo(photo=photo, caption=f"{msg}")
    await message.answer(f"Отправить?", reply_markup=SU_accept_send_kb)
    await state.update_data(photo_or_text="photo", photo=photo, msg=msg)


@dp.callback_query_handler(text="su_send_msg_accept", state=SU.msg_text_date)
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f"Начата отправка сообщений.\n"
                                 f"\n"
                                 f"Это может занять некоторое время, пожалуйста, ожидайте")
    data = await state.get_data()
    users = data.get("users")
    photo_or_text = data.get("photo_or_text")
    if photo_or_text == "text":
        msg = data.get("msg")
        for user in users:
            try:
                await bot.send_message(chat_id=user.id, text=msg)
            except:
                pass
        await call.message.edit_text(f"Все сообщения отправлены", reply_markup=SU_to_main_kb)
    if photo_or_text == "photo":
        photo = data.get("photo")
        msg = data.get("msg")
        for user in users:
            try:
                if msg is None:
                    await bot.send_photo(chat_id=user.id, photo=photo)
                else:
                    await bot.send_photo(chat_id=user.id, photo=photo, caption=msg)
            except:
                pass
        await call.message.edit_text(f"Все сообщения отправлены", reply_markup=SU_to_main_kb)
    await state.finish()


@dp.callback_query_handler(text="SU_msg_age")
async def def_mame(call: types.CallbackQuery):
    total_users = await qc.count_users()
    total_male = await qc.count_users_sex(sex="Male")
    total_female = await qc.count_users_sex(sex="Female")
    total_ru = await qc.count_users_language(language="ru")
    total_ru_m = await qc.count_users_sex_language(sex="Male", language="ru")
    total_ru_f = await qc.count_users_sex_language(sex="Female", language="ru")
    total_en = await qc.count_users_language(language="en")
    total_en_m = await qc.count_users_sex_language(sex="Male", language="en")
    total_en_f = await qc.count_users_sex_language(sex="Female", language="en")
    total_es = await qc.count_users_language(language="es")
    total_es_m = await qc.count_users_sex_language(sex="Male", language="es")
    total_es_f = await qc.count_users_sex_language(sex="Female", language="es")
    total_de = await qc.count_users_language(language="de")
    total_de_m = await qc.count_users_sex_language(sex="Male", language="de")
    total_de_f = await qc.count_users_sex_language(sex="Female", language="de")
    referrals = await qc.count_users_referrers()
    await call.message.edit_text(f"👩‍👦‍👦Всего пользователей: {total_users}\n"
                                 f"🙍‍♀️ Женщин: {total_female}\n"
                                 f"🙍‍♂️ Мужчин: {total_male}\n"
                                 f"\n"
                                 f"🇷🇺 Пользователей: {total_ru}\n"
                                 f"🇷🇺🙍‍♀️ Женщин: {total_ru_f}\n"
                                 f"🇷🇺🙍‍♂️ Мужчин: {total_ru_m}\n"
                                 f"\n"
                                 f"🇺🇸 Пользователей: {total_en}\n"
                                 f"🇺🇸🙍‍♀️ Женщин: {total_en_f}\n"
                                 f"🇺🇸🙍‍♂️ Мужчин: {total_en_m}\n"
                                 f"\n"
                                 f"🇪🇸 Пользователей: {total_es}\n"
                                 f"🇪🇸🙍‍♀️ Женщин: {total_es_f}\n"
                                 f"🇪🇸🙍‍♂️ Мужчин: {total_es_m}\n"
                                 f"\n"
                                 f"🇩🇪 Пользователей: {total_de}\n"
                                 f"🇩🇪🙍‍♀️ Женщин: {total_de_f}\n"
                                 f"🇩🇪🙍‍♂️ Мужчин: {total_de_m}\n", reply_markup=SU_msg_language_kb)
    await SU.msg_via_age.set()


@dp.callback_query_handler(Text(equals=["SU_msg_ru_all", "SU_msg_ru_female", "SU_msg_ru_male",
                                        "SU_msg_en_all", "SU_msg_en_female", "SU_msg_en_male",
                                        "SU_msg_es_all", "SU_msg_es_female", "SU_msg_es_male",
                                        "SU_msg_de_all", "SU_msg_de_female", "SU_msg_de_male"]), state=SU.msg_via_age)
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    type_people = call.data
    if type_people == "SU_msg_ru_all":
        people = await qc.get_users_language(language="ru")
        text = "с языком RU (и мужчинам и женщинам)"
        language = "ru"
        sex = "All"
    if type_people == "SU_msg_en_all":
        people = await qc.get_users_language(language="en")
        text = "с языком EN (и мужчинам и женщинам)"
        language = "en"
        sex = "All"
    if type_people == "SU_msg_es_all":
        people = await qc.get_users_language(language="es")
        text = "с языком ES (и мужчинам и женщинам)"
        language = "es"
        sex = "All"
    if type_people == "SU_msg_de_all":
        people = await qc.get_users_language(language="de")
        text = "с языком DE (и мужчинам и женщинам)"
        language = "de"
        sex = "All"
    if type_people == "SU_msg_ru_female":
        people = await qc.get_users_language_and_sex(language="ru", sex="Female")
        text = "с языком RU (только женщинам)"
        language = "ru"
        sex = "Female"
    if type_people == "SU_msg_en_female":
        people = await qc.get_users_language_and_sex(language="en", sex="Female")
        text = "с языком EN (только женщинам)"
        language = "en"
        sex = "Female"
    if type_people == "SU_msg_es_female":
        people = await qc.get_users_language_and_sex(language="es", sex="Female")
        text = "с языком ES (только женщинам)"
        language = "es"
        sex = "Female"
    if type_people == "SU_msg_de_female":
        people = await qc.get_users_language_and_sex(language="de", sex="Female")
        text = "с языком DE (только женщинам)"
        language = "de"
        sex = "Female"
    if type_people == "SU_msg_ru_male":
        people = await qc.get_users_language_and_sex(language="ru", sex="Male")
        text = "с языком RU (только мужчинам)"
        language = "ru"
        sex = "Male"
    if type_people == "SU_msg_en_male":
        people = await qc.get_users_language_and_sex(language="en", sex="Male")
        text = "с языком EN (только мужчинам)"
        language = "en"
        sex = "Male"
    if type_people == "SU_msg_es_male":
        people = await qc.get_users_language_and_sex(language="es", sex="Male")
        text = "с языком ES (только мужчинам)"
        language = "es"
        sex = "Male"
    if type_people == "SU_msg_de_male":
        people = await qc.get_users_language_and_sex(language="de", sex="Male")
        text = "с языком DE (только мужчинам)"
        language = "de"
        sex = "Male"
    x = 0
    for man in people:
        x += 1
    if x == 0:
        await call.message.edit_text(f"По заданным фильтрам людей нет.\n"
                                     f"Измените критерии поиска", reply_markup=SU_msg_language_kb)
    else:
        await call.message.edit_text(f"Вы собираетесь отправить сообщение людям {text}.\n"
                                     f"\n"
                                     f"Выберите подходящий фильтр по возрасту", reply_markup=SU_via_age_kb)
        await state.update_data(people=f" людям {text}", language=language, sex=sex)


@dp.callback_query_handler(Text(equals=["after_age", "before_age", "select_age"]), state=SU.msg_via_age)
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    people = data.get("people")
    type_age = call.data
    if type_age == "after_age":
        await call.message.edit_text(f"Вы собираетесь отправить сообщение {people}, которые родились после ХХХХ года.\n"
                                  f"\n"
                                  f"Укажите год\n"
                                  f"Например 2000 - значит отправить всем, кто родился в 2000, 2001, 2002... (то есть младше 21 года)", reply_markup=SU_to_main_kb)
        await state.update_data(type_age="after_age")
    if type_age == "before_age":
        await call.message.edit_text(f"Вы собираетесь отправить сообщение {people}, которые родились раньше ХХХХ года.\n"
                                  f"\n"
                                  f"Укажите год\n"
                                  f"Например 2000 - значит отправить всем, кто родился в 2000, 1999, 1998... (то есть старше 21 года)", reply_markup=SU_to_main_kb)
        await state.update_data(type_age="before_age")
    if type_age == "select_age":
        await call.message.edit_text(f"Вы собираетесь отправить сообщение {people}, которые родились в ХХХХ год.\n"
                                  f"\n"
                                  f"Укажите год\n"
                                  f"Например 2000 - значит отправить всем, кто родился в 2000 году", reply_markup=SU_to_main_kb)
        await state.update_data(type_age="select_age")
    await SU.msg_select_age.set()



@dp.message_handler(state=SU.msg_select_age)
async def def_name(message: types.Message, state: FSMContext):
    year = message.text
    try:
        year = int(year)
        data = await state.get_data()
        type_age = data.get("type_age")
        people = data.get("people")
        language = data.get("language")
        sex = data.get("sex")
        if type_age == "after_age":
            if sex in ("Female", "Male"):
                users = await qc.get_users_language_and_age_after(language=language, sex=sex, year=str(year))
            else:
                users = await qc.get_users_language_and_age_after_no_sex(language=language, year=str(year))
            qty = 0
            for user in users:
                qty += 1
            if qty == 0:
                await message.answer(f"🔴Людей {people}, которые родились после {year} года НЕТ\n"
                                      f"\n"
                                      f"Укажите другой год рождения или вернитесь в главное меню", reply_markup=SU_to_main_kb)
            else:
                await message.answer(f"Вы собираетесь отправить сообщение людям {people}, которые родились после {year} года (Таких людей {qty} шт)\n"
                                     f"\n"
                                     f"Напишите текст сообщения.\n"
                                     f"Если хотите отправить фото - прикрепите фотографию и в описание добавьте текст", reply_markup=SU_to_main_kb)
                await state.update_data(users=users, year=year, qty=qty)
                await SU.msg_text_age.set()
        if type_age == "before_age":
            if sex in ("Female", "Male"):
                users = await qc.get_users_language_and_age_before(language=language, sex=sex, year=str(year))
            else:
                users = await qc.get_users_language_and_age_before_no_sex(language=language, year=str(year))
            qty = 0
            for user in users:
                qty += 1
            if qty == 0:
                await message.answer(f"🔴Людей {people}, которые родились до {year} года НЕТ\n"
                                      f"\n"
                                      f"Укажите другой год рождения или вернитесь в главное меню", reply_markup=SU_to_main_kb)
            else:
                await message.answer(f"Вы собираетесь отправить сообщение людям {people}, которые родились до {year} года (Таких людей {qty} шт)\n"
                                     f"\n"
                                     f"Напишите текст сообщения.\n"
                                     f"Если хотите отправить фото - прикрепите фотографию и в описание добавьте текст", reply_markup=SU_to_main_kb)
                await state.update_data(users=users, year=year, qty=qty)
                await SU.msg_text_age.set()
        if type_age == "select_age":
            if sex in ("Female", "Male"):
                users = await qc.get_users_language_and_age_select(language=language, sex=sex, year=str(year))
            else:
                users = await qc.get_users_language_and_age_select_no_sex(language=language, year=str(year))
            qty = 0
            for user in users:
                qty += 1
            if qty == 0:
                await message.answer(f"🔴Людей {people}, которые родились в {year} год года НЕТ\n"
                                      f"\n"
                                      f"Укажите другой год рождения или вернитесь в главное меню", reply_markup=SU_to_main_kb)
            else:
                await message.answer(f"Вы собираетесь отправить сообщение людям {people}, которые родились в {year} год (Таких людей {qty} шт)\n"
                                     f"\n"
                                     f"Напишите текст сообщения.\n"
                                     f"Если хотите отправить фото - прикрепите фотографию и в описание добавьте текст", reply_markup=SU_to_main_kb)
                await state.update_data(users=users, year=year, qty=qty)
                await SU.msg_text_age.set()
    except:
        await message.answer(f"Вы неправильно указали год. Укажите его в формате 1995", reply_markup=SU_to_main_kb)


@dp.message_handler(content_types=ContentTypes.TEXT, state=SU.msg_text_age)
async def def_name(message: types.Message, state: FSMContext):
    msg = message.text
    data = await state.get_data()
    people = data.get("people")
    type_age = data.get("type_age")
    year = data.get("year")
    qty = data.get("qty")

    if type_age == "after_age":
        await message.answer(f"Вы собираетесь отправить сообщение {qty} людям {people}, которые родились после {year} года\n"
                             f"\n"
                             f"Оно будет выглядеть так:", reply_markup=SU_to_main_kb)
    if type_age == "before_age":
        await message.answer(f"Вы собираетесь отправить сообщение {qty} людям {people}, которые родились до {year} года\n"
                             f"\n"
                             f"Оно будет выглядеть так:",
                             reply_markup=SU_to_main_kb)
    if type_age == "select_age":
        await message.answer(f"Вы собираетесь отправить сообщение {qty} людям {people}, которые родились в {year} год\n"
                             f"\n"
                             f"Оно будет выглядеть так:",
                             reply_markup=SU_to_main_kb)
    await message.answer(f"{msg}")
    await message.answer(f"Отправить?", reply_markup=SU_accept_send_kb)
    await state.update_data(photo_or_text="text", msg=msg)


@dp.message_handler(content_types=ContentTypes.PHOTO, state=SU.msg_text_age)
async def def_name(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    msg = message.caption
    data = await state.get_data()
    people = data.get("people")
    type_age = data.get("type_age")
    year = data.get("year")
    qty = data.get("qty")
    if type_age == "after_age":
        await message.answer(f"Вы собираетесь отправить сообщение {qty} людям {people}, которые родились после {year} года\n"
                             f"\n"
                             f"Оно будет выглядеть так:", reply_markup=SU_to_main_kb)
    if type_age == "before_age":
        await message.answer(f"Вы собираетесь отправить сообщение {qty} людям {people}, которые родились до {year} года\n"
                             f"\n"
                             f"Оно будет выглядеть так:",
                             reply_markup=SU_to_main_kb)
    if type_age == "select_age":
        await message.answer(f"Вы собираетесь отправить сообщение {qty} людям {people}, которые родились в {year} год\n"
                             f"\n"
                             f"Оно будет выглядеть так:",
                             reply_markup=SU_to_main_kb)
    if msg is None:
        await message.answer_photo(photo=photo)
    else:
        await message.answer_photo(photo=photo, caption=f"{msg}")
    await message.answer(f"Отправить?", reply_markup=SU_accept_send_kb)
    await state.update_data(photo_or_text="photo", photo=photo, msg=msg)


@dp.callback_query_handler(text="su_send_msg_accept", state=SU.msg_text_age)
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f"Начата отправка сообщений.\n"
                                 f"\n"
                                 f"Это может занять некоторое время, пожалуйста, ожидайте")
    data = await state.get_data()
    users = data.get("users")
    photo_or_text = data.get("photo_or_text")
    if photo_or_text == "text":
        msg = data.get("msg")
        for user in users:
            try:
                await bot.send_message(chat_id=user.id, text=msg)
            except:
                pass
        await call.message.edit_text(f"Все сообщения отправлены", reply_markup=SU_to_main_kb)
    if photo_or_text == "photo":
        photo = data.get("photo")
        msg = data.get("msg")
        for user in users:
            try:
                if msg is None:
                    await bot.send_photo(chat_id=user.id, photo=photo)
                else:
                    await bot.send_photo(chat_id=user.id, photo=photo, caption=msg)
            except:
                pass
        await call.message.edit_text(f"Все сообщения отправлены", reply_markup=SU_to_main_kb)
    await state.finish()


@dp.callback_query_handler(text="SU_msg_language")
async def def_mame(call: types.CallbackQuery):
    total_users = await qc.count_users()
    total_male = await qc.count_users_sex(sex="Male")
    total_female = await qc.count_users_sex(sex="Female")
    total_ru = await qc.count_users_language(language="ru")
    total_ru_m = await qc.count_users_sex_language(sex="Male", language="ru")
    total_ru_f = await qc.count_users_sex_language(sex="Female", language="ru")
    total_en = await qc.count_users_language(language="en")
    total_en_m = await qc.count_users_sex_language(sex="Male", language="en")
    total_en_f = await qc.count_users_sex_language(sex="Female", language="en")
    total_es = await qc.count_users_language(language="es")
    total_es_m = await qc.count_users_sex_language(sex="Male", language="es")
    total_es_f = await qc.count_users_sex_language(sex="Female", language="es")
    total_de = await qc.count_users_language(language="de")
    total_de_m = await qc.count_users_sex_language(sex="Male", language="de")
    total_de_f = await qc.count_users_sex_language(sex="Female", language="de")
    referrals = await qc.count_users_referrers()
    await call.message.edit_text(f"👩‍👦‍👦Всего пользователей: {total_users}\n"
                                 f"🙍‍♀️ Женщин: {total_female}\n"
                                 f"🙍‍♂️ Мужчин: {total_male}\n"
                                 f"\n"
                                 f"🇷🇺 Пользователей: {total_ru}\n"
                                 f"🇷🇺🙍‍♀️ Женщин: {total_ru_f}\n"
                                 f"🇷🇺🙍‍♂️ Мужчин: {total_ru_m}\n"
                                 f"\n"
                                 f"🇺🇸 Пользователей: {total_en}\n"
                                 f"🇺🇸🙍‍♀️ Женщин: {total_en_f}\n"
                                 f"🇺🇸🙍‍♂️ Мужчин: {total_en_m}\n"
                                 f"\n"
                                 f"🇪🇸 Пользователей: {total_es}\n"
                                 f"🇪🇸🙍‍♀️ Женщин: {total_es_f}\n"
                                 f"🇪🇸🙍‍♂️ Мужчин: {total_es_m}\n"
                                 f"\n"
                                 f"🇩🇪 Пользователей: {total_de}\n"
                                 f"🇩🇪🙍‍♀️ Женщин: {total_de_f}\n"
                                 f"🇩🇪🙍‍♂️ Мужчин: {total_de_m}\n", reply_markup=SU_msg_language_kb)
    await SU.msg_via_language.set()


@dp.callback_query_handler(Text(equals=["SU_msg_ru_all", "SU_msg_ru_female", "SU_msg_ru_male",
                                        "SU_msg_en_all", "SU_msg_en_female", "SU_msg_en_male",
                                        "SU_msg_es_all", "SU_msg_es_female", "SU_msg_es_male",
                                        "SU_msg_de_all", "SU_msg_de_female", "SU_msg_de_male"]), state=SU.msg_via_language)
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    type_people = call.data
    if type_people == "SU_msg_ru_all":
        people = await qc.get_users_language(language="ru")
        text = "С языком RU (и мужчинам и женщинам)"
    if type_people == "SU_msg_en_all":
        people = await qc.get_users_language(language="en")
        text = "С языком EN (и мужчинам и женщинам)"
    if type_people == "SU_msg_es_all":
        people = await qc.get_users_language(language="es")
        text = "С языком ES (и мужчинам и женщинам)"
    if type_people == "SU_msg_de_all":
        people = await qc.get_users_language(language="de")
        text = "С языком DE (и мужчинам и женщинам)"
    if type_people == "SU_msg_ru_female":
        people = await qc.get_users_language_and_sex(language="ru", sex="Female")
        text = "С языком RU (только женщинам)"
    if type_people == "SU_msg_en_female":
        people = await qc.get_users_language_and_sex(language="en", sex="Female")
        text = "С языком EN (только женщинам)"
    if type_people == "SU_msg_es_female":
        people = await qc.get_users_language_and_sex(language="es", sex="Female")
        text = "С языком ES (только женщинам)"
    if type_people == "SU_msg_de_female":
        people = await qc.get_users_language_and_sex(language="de", sex="Female")
        text = "С языком DE (только женщинам)"
    if type_people == "SU_msg_ru_male":
        people = await qc.get_users_language_and_sex(language="ru", sex="Male")
        text = "С языком RU (только мужчинам)"
    if type_people == "SU_msg_en_male":
        people = await qc.get_users_language_and_sex(language="en", sex="Male")
        text = "С языком EN (только мужчинам)"
    if type_people == "SU_msg_es_male":
        people = await qc.get_users_language_and_sex(language="es", sex="Male")
        text = "С языком ES (только мужчинам)"
    if type_people == "SU_msg_de_male":
        people = await qc.get_users_language_and_sex(language="de", sex="Male")
        text = "С языком DE (только мужчинам)"
    x = 0
    for man in people:
        x += 1
    if x == 0:
        await call.message.edit_text(f"По заданным фильтрам людей нет.\n"
                                     f"Измените критерии поиска", reply_markup=SU_msg_language_kb)
    else:
        await call.message.edit_text(f"Вы собираетесь отправить сообщение {x} людям, {text}.\n"
                                     f"\n"
                                     f"Напишите текст сообщения.\n"
                                     f"Если хотите отправить фото - прикрепите фотографию и в описание добавьте текст\n"
                                     f"\n"
                                     f"Что бы отменить - нажмите на кнопку", reply_markup=SU_to_main_kb)
        await state.update_data(people=f"{x} людям, {text}", users=people)


@dp.message_handler(content_types=ContentTypes.TEXT, state=SU.msg_via_language)
async def def_name(message: types.Message, state: FSMContext):
    msg = message.text
    data = await state.get_data()
    people = data.get("people")
    await message.answer(f"Вы собираетесь отправить {people} сообщение.\n"
                         f"\n"
                         f"Оно будет выглядеть так:")
    await message.answer(f"{msg}")
    await message.answer(f"Отправить?", reply_markup=SU_accept_send_kb)
    await state.update_data(photo_or_text="text", msg=msg)


@dp.message_handler(content_types=ContentTypes.PHOTO, state=SU.msg_via_language)
async def def_name(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    msg = message.caption
    data = await state.get_data()
    people = data.get("people")
    await message.answer(f"Вы собираетесь отправить {people} сообщение.\n"
                         f"\n"
                         f"Оно будет выглядеть так:")
    if msg is None:
        await message.answer_photo(photo=photo)
    else:
        await message.answer_photo(photo=photo, caption=f"{msg}")
    await message.answer(f"Отправить?", reply_markup=SU_accept_send_kb)
    await state.update_data(photo_or_text="photo", photo=photo, msg=msg)


@dp.message_handler(content_types=ContentTypes.ANY, state=SU.msg_via_language)
async def def_name(message: types.Message, state: FSMContext):
    await message.answer(f"Вы можете отправить текст или фото. Повторите попытку\n"
                         f"\n"
                         f"Что бы отменить - нажмите на кнопку", reply_markup=SU_to_main_kb)


@dp.callback_query_handler(text="su_send_msg_accept", state=SU.msg_via_language)
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(f"Начата отправка сообщений.\n"
                                 f"\n"
                                 f"Это может занять некоторое время, пожалуйста, ожидайте")
    data = await state.get_data()
    users = data.get("users")
    photo_or_text = data.get("photo_or_text")
    if photo_or_text == "text":
        msg = data.get("msg")
        for user in users:
            try:
                await bot.send_message(chat_id=user.id, text=msg)
            except:
                pass
        await call.message.edit_text(f"Все сообщения отправлены", reply_markup=SU_to_main_kb)
    if photo_or_text == "photo":
        photo = data.get("photo")
        msg = data.get("msg")
        for user in users:
            try:
                if msg is None:
                    await bot.send_photo(chat_id=user.id, photo=photo)
                else:
                    await bot.send_photo(chat_id=user.id, photo=photo, caption=msg)
            except:
                pass
        await call.message.edit_text(f"Все сообщения отправлены", reply_markup=SU_to_main_kb)
    await state.finish()


@dp.callback_query_handler(text="stat")
async def def_mame(call: types.CallbackQuery):
    total_users = await qc.count_users()
    total_male = await qc.count_users_sex(sex="Male")
    total_female = await qc.count_users_sex(sex="Female")
    total_ru = await qc.count_users_language(language="ru")
    total_ru_m = await qc.count_users_sex_language(sex="Male", language="ru")
    total_ru_f = await qc.count_users_sex_language(sex="Female", language="ru")
    total_en = await qc.count_users_language(language="en")
    total_en_m = await qc.count_users_sex_language(sex="Male", language="en")
    total_en_f = await qc.count_users_sex_language(sex="Female", language="en")
    total_es = await qc.count_users_language(language="es")
    total_es_m = await qc.count_users_sex_language(sex="Male", language="es")
    total_es_f = await qc.count_users_sex_language(sex="Female", language="es")
    total_de = await qc.count_users_language(language="de")
    total_de_m = await qc.count_users_sex_language(sex="Male", language="de")
    total_de_f = await qc.count_users_sex_language(sex="Female", language="de")
    referrals = await qc.count_users_referrers()
    await call.message.edit_text(f"👩‍👦‍👦Всего пользователей: {total_users}\n"
                                 f"🙍‍♀️ Женщин: {total_female}\n"
                                 f"🙍‍♂️ Мужчин: {total_male}\n"
                                 f"\n"
                                 f"🇷🇺 Пользователей: {total_ru}\n"
                                 f"🇷🇺🙍‍♀️ Женщин: {total_ru_f}\n"
                                 f"🇷🇺🙍‍♂️ Мужчин: {total_ru_m}\n"
                                 f"\n"
                                 f"🇺🇸 Пользователей: {total_en}\n"
                                 f"🇺🇸🙍‍♀️ Женщин: {total_en_f}\n"
                                 f"🇺🇸🙍‍♂️ Мужчин: {total_en_m}\n"
                                 f"\n"
                                 f"🇪🇸 Пользователей: {total_es}\n"
                                 f"🇪🇸🙍‍♀️ Женщин: {total_es_f}\n"
                                 f"🇪🇸🙍‍♂️ Мужчин: {total_es_m}\n"
                                 f"\n"
                                 f"🇩🇪 Пользователей: {total_de}\n"
                                 f"🇩🇪🙍‍♀️ Женщин: {total_de_f}\n"
                                 f"🇩🇪🙍‍♂️ Мужчин: {total_de_m}\n"
                                 f"\n"
                                 f"Пользователи пригласили людей: {referrals}\n"
                                 f"Пользователи нашли бота сами: {total_users - referrals}", reply_markup=main_SU_kb)

