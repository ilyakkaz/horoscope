from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text

from keyboards.default.main_kb import menu_de, menu_es, menu_en, menu_ru
from keyboards.default.profile_default_kb import profile_de, profile_es, profile_en, profile_ru, settings_profile_de, \
    settings_profile_es, settings_profile_en, settings_profile_ru
from keyboards.inline.notify_kb import notify_time_kb, on_off_ru, edit_notify_time_kb_ru, \
    edit_notify_time_kb_en, edit_notify_time_kb_es, edit_notify_time_kb_de, on_off_de, on_off_es, on_off_en
from keyboards.inline.start_kb import language_kb, skip_time_ru, skip_time_en, skip_time_es, skip_time_de, time_zone_kb
from states.states import Compatibility, Settings, Profile, Pifagor
from utils.db_api import quick_commands as qc

from loader import dp


@dp.message_handler(Text(equals=["Профиль", "Profile", "Perfil", "Profil"]), state="*")
async def select_compatibility(message: types.Message, state: FSMContext):
    user = await qc.get_user(id=int(message.from_user.id))
    if user.language == "ru":
        await message.answer(f"Добро пожаловать в ваш профиль", reply_markup=profile_ru)
    if user.language == "en":
        await message.answer(f"Welcome to your profile", reply_markup=profile_en)
    if user.language == "es":
        await message.answer(f"Bienvenido a tu perfil", reply_markup=profile_es)
    if user.language == "de":
        await message.answer(f"Willkommen in Ihrem Profil", reply_markup=profile_de)
    await state.finish()


@dp.message_handler(text="Профиль", state="*")
async def select_compatibility(message: types.Message, state: FSMContext):
    user = await qc.get_user(id=int(message.from_user.id))
    if user.language == "ru":
        await message.answer(f"Добро пожаловать в ваш профиль", reply_markup=profile_ru)
    if user.language == "en":
        await message.answer(f"Welcome to your profile", reply_markup=profile_en)
    if user.language == "es":
        await message.answer(f"Bienvenido a tu perfil", reply_markup=profile_es)
    if user.language == "de":
        await message.answer(f"Willkommen in Ihrem Profil", reply_markup=profile_de)
    await state.finish()


@dp.message_handler(Text(equals=["Настройки", "Settings", "Ajustes", "die Einstellungen"]))
async def def_mame(message: types.Message):
    user = await qc.get_user(id=int(message.from_user.id))
    if user.language == "ru":
        await message.answer(f"Настройки", reply_markup=settings_profile_ru)
    if user.language == "en":
        await message.answer(f"Settings", reply_markup=settings_profile_en)
    if user.language == "es":
        await message.answer(f"Ajustes", reply_markup=settings_profile_es)
    if user.language == "de":
        await message.answer(f"die Einstellungen",
                             reply_markup=settings_profile_de)


@dp.message_handler(Text(equals=["Изменить язык", "Change the language", "Cambia el idioma", "Ändere die Sprache"]),
                    state='*')
async def def_mame(message: types.Message):
    user = await qc.get_user(id=int(message.from_user.id))
    if user.language == "ru":
        await message.answer(f"Выберите язык", reply_markup=language_kb)
    if user.language == "en":
        await message.answer(
            f"Choose language", reply_markup=language_kb)
    if user.language == "es":
        await message.answer(
            f"Elige lengua", reply_markup=language_kb)
    if user.language == "de":
        await message.answer(
            f"Sprache wählen", reply_markup=language_kb)
    await Settings.language.set()


@dp.callback_query_handler(Text(equals=["ru", "en", "es", "de"]), state=Settings.language)
async def language(call: types.CallbackQuery, state: FSMContext):
    language = call.data
    await call.message.delete()
    if language == "ru":
        await call.message.answer(f"🇷🇺", reply_markup=menu_ru)
        await call.message.answer(f"Вы успешно изменили язык", reply_markup=menu_ru)
    if language == "en":
        await call.message.answer(f"🇺🇸", reply_markup=menu_en)
        await call.message.answer(f"You have successfully changed the language", reply_markup=menu_en)
    if language == "es":
        await call.message.answer(f"🇪🇸", reply_markup=menu_es)
        await call.message.answer(f"Has cambiado el idioma con éxito", reply_markup=menu_es)
    if language == "de":
        await call.message.answer(f"🇩🇪", reply_markup=menu_de)
        await call.message.answer(f"Sie haben die Sprache erfolgreich geändert", reply_markup=menu_de)
    await qc.update_language(id=int(call.from_user.id), language=language)
    await state.finish()


@dp.message_handler(Text(equals=["Квадрат пифагора", "Pythagoras square", "Plaza de pitágoras", "Pythagoras-Platz"]))
async def language(message: types.Message, state: FSMContext):
    user = await qc.get_user(id=int(message.from_user.id))
    if user.language == "ru":
        await message.answer(f"Для расчета квадрата пифагора введите дату рождения\n"
                             f"\n"
                             f"<i>Например 21.04.1990</i>")
    if user.language == "en":
        await message.answer(f"To calculate the square of Pythagoras, enter date of birth\n"
                             f"\n"
                             f"<i>For example 04/21/1990</i>")
    if user.language == "es":
        await message.answer(f"Para calcular el cuadrado de Pitágoras, ingrese su fecha de nacimiento\n"
                             f"\n"
                             f"<i>Por ejemplo 21/04/1990</i>")
    if user.language == "de":
        await message.answer(f"Um das Quadrat von Pythagoras zu berechnen, geben Sie Ihr Geburtsdatum ein\n"
                             f"\n"
                             f"<i>Zum Beispiel 21.04.1990</i>")
    await Pifagor.date.set()

@dp.message_handler(Text(equals=["Уведомления", "Notifications", "Notificaciones", "Benachrichtigungen", ""]),
                    state='*')
async def language(message: types.Message, state: FSMContext):
    user = await qc.get_user(id=int(message.from_user.id))
    if user.language == "ru":
        user = await qc.get_user(id=int(message.from_user.id))
        time_zone = user.time_zone
        notify_time = user.notify_time
        if notify_time is None:
            await message.answer(f"Ваш часовой пояс: {time_zone}\n"
                                 f"Время получения гороскопа не указано, выберите время",
                                 reply_markup=notify_time_kb)
        elif notify_time == "default" and user.notify_horo == "Общий, ":
            await message.answer(f"Ваш часовой пояс: {time_zone}\n"
                                 f"Вы можете выбрать время, в которое вам будут приходить уведомления и гороскопы, которые вы хотите видеть",
                                 reply_markup=edit_notify_time_kb_ru)
        else:
            if user.notify_horo:
                selected_horoscope = user.notify_horo
            else:
                selected_horoscope = "Нет выбранных гороскопов (уведомления не будут приходить)"
            await message.answer(f"Ваш часовой пояс: {time_zone}\n"
                                 f"\n"
                                 f"Выбранные гороскопы: {selected_horoscope}",
                                 reply_markup=edit_notify_time_kb_ru)
    if user.language == "en":
        user = await qc.get_user(id=int(message.from_user.id))
        time_zone = user.time_zone
        notify_time = user.notify_time
        if notify_time is None:
            await message.answer(f"Your time zone: {time_zone}\n"
                                 f"\n"
                                 f"The time of receiving the horoscope is not specified, please select a time",
                                 reply_markup=notify_time_kb)
        elif notify_time == "default" and user.notify_horo == "Общий, ":
            await message.answer(f"Your time zone: {time_zone}\n"
                                 f"\n"
                                 f"At 19:00 you will receive a general horoscope for tomorrow.",
                                 reply_markup=edit_notify_time_kb_en)
        else:
            if user.notify_horo:
                selected_horoscope = user.notify_horo
            else:
                selected_horoscope = "There are no selected horoscopes (notifications will not come)"
            text = f"{selected_horoscope}"
            try:
                text = text.replace("Любовный,", "Love")
                text = text.replace("Общий,", "General")
                text = text.replace("Деловой,", "Business")
            except:
                pass
            await message.answer(f"Your time zone: {time_zone}\n"
                                 f"\n"
                                 f"Selected horoscopes: {text}",
                                 reply_markup=edit_notify_time_kb_en)
    if user.language == "es":
        user = await qc.get_user(id=int(message.from_user.id))
        time_zone = user.time_zone
        notify_time = user.notify_time
        if notify_time is None:
            await message.answer(f"Tu zona horaria: {time_zone}\n"
                                 f"La hora de recibir el horóscopo no está especificada, seleccione una hora",
                                 reply_markup=notify_time_kb)
        elif notify_time == "default" and user.notify_horo == "Общий, ":
            await message.answer(f"Tu zona horaria: {time_zone}\n"
                                 f"A las 19:00 horas recibirás un horóscopo general para mañana.",
                                 reply_markup=edit_notify_time_kb_es)
        else:
            if user.notify_horo:
                selected_horoscope = user.notify_horo
            else:
                selected_horoscope = "No hay horóscopos seleccionados (no recibirán notificaciones)"
            text = f"{selected_horoscope}"
            try:
                text = text.replace("Любовный,", "Amor")
                text = text.replace("Общий,", "General")
                text = text.replace("Деловой,", "Negocio")
            except:
                pass
            await message.answer(f"Tu zona horaria: {time_zone}\n"
                                 f"\n"
                                 f"Horóscopos seleccionados: {text}",
                                 reply_markup=edit_notify_time_kb_es)
    if user.language == "de":
        user = await qc.get_user(id=int(message.from_user.id))
        time_zone = user.time_zone
        notify_time = user.notify_time
        if notify_time is None:
            await message.answer(f"Deine Zeitzone: {time_zone}\n"
                                 f"\n"
                                 f"Der Zeitpunkt des Erhalts des Horoskops ist nicht angegeben, bitte wählen Sie einen Zeitpunkt",
                                 reply_markup=notify_time_kb)
        elif notify_time == "default" and user.notify_horo == "Общий, ":
            await message.answer(f"Deine Zeitzone: {time_zone}\n"
                                 f"\n"
                                 f"Um 19:00 erhalten Sie ein allgemeines Horoskop für morgen.",
                                 reply_markup=edit_notify_time_kb_de)
        else:
            if user.notify_horo:
                selected_horoscope = user.notify_horo
            else:
                selected_horoscope = "Es gibt keine ausgewählten Horoskope (Benachrichtigungen werden nicht kommen)"
            text = f"{selected_horoscope}"
            try:
                text = text.replace("Любовный,", "Liebe")
                text = text.replace("Общий,", "Allgemein")
                text = text.replace("Деловой,", "Geschäft")
            except:
                pass
            await message.answer(f"Deine Zeitzone: {time_zone}\n"
                                 f"\n"
                                 f"Ausgewählte Horoskope: {text}",
                                 reply_markup=edit_notify_time_kb_de)
    await state.finish()


@dp.callback_query_handler(text="select_horo")
async def def_mame(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    if user.notify_horo:
        selected_horoscope = user.notify_horo
    else:
        selected_horoscope = "Нет выбранных гороскопов (уведомления не будут приходить)"
    text = f"Выбранные горосокопы:\n" \
           f"\n" \
           f"{selected_horoscope}"
    if user.language == "ru":
        await call.message.edit_text(f"{text}", reply_markup=on_off_ru)
    if user.language == "en":
        try:
            text = text.replace("Выбранные горосокопы", "Selected horoscopes")
            text = text.replace("Любовный,", "Love")
            text = text.replace("Общий,", "General")
            text = text.replace("Деловой,", "Business")
            text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)", "There are no selected horoscopes (notifications will not come)")
        except:
            pass
        await call.message.edit_text(f"{text}", reply_markup=on_off_en)
    if user.language == "es":
        try:
            text = text.replace("Выбранные горосокопы", "Horóscopos seleccionados")
            text = text.replace("Любовный,", "Amor")
            text = text.replace("Общий,", "General")
            text = text.replace("Деловой,", "Negocio")
            text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)", "No hay horóscopos seleccionados (no recibirán notificaciones)")
        except:
            pass
        await call.message.edit_text(f"{text}", reply_markup=on_off_es)
    if user.language == "de":
        try:
            text = text.replace("Выбранные горосокопы", "Ausgewählte Horoskope")
            text = text.replace("Любовный,", "Liebe")
            text = text.replace("Общий,", "Allgemein")
            text = text.replace("Деловой,", "Geschäft")
            text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)", "Es gibt keine ausgewählten Horoskope (Benachrichtigungen werden nicht kommen)")
        except:
            pass
        await call.message.edit_text(f"{text}", reply_markup=on_off_de)


@dp.callback_query_handler(text="on_off_love")
async def def_mame(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    if user.notify_horo:
        print("if 1")
        selected_horoscope = str(user.notify_horo)
        selected_horoscope_split = user.notify_horo.split()
        x = 0
        z = 0
        for y in selected_horoscope_split:
            z += 1
        for i in selected_horoscope_split:
            print("for i")
            if i == "Любовный,":
                print("if 2")
                text = str(selected_horoscope).replace("Любовный, ", "")
                await qc.update_selected_horo(id=int(call.from_user.id), text=text)
            else:
                x += 1
        if x >= z:
            print("else 2")
            text = selected_horoscope + "Любовный, "
            await qc.update_selected_horo(id=int(call.from_user.id), text=text)
    else:
        print("else 1")
        text = "Любовный, "
        await qc.update_selected_horo(id=call.from_user.id, text=text)
    user_upd = await qc.get_user(id=int(call.from_user.id))
    if user_upd.notify_horo:
        text = f"Выбранные горосокопы:\n" \
               f"\n" \
               f"{user_upd.notify_horo}"
        if user.language == "ru":
            await call.message.edit_text(f"{text}", reply_markup=on_off_ru)
        if user.language == "en":
            try:
                text = text.replace("Выбранные горосокопы", "Selected horoscopes")
                text = text.replace("Любовный,", "Love")
                text = text.replace("Общий,", "General")
                text = text.replace("Деловой,", "Business")
                text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)",
                                    "There are no selected horoscopes (notifications will not come)")
            except:
                pass
            await call.message.edit_text(f"{text}", reply_markup=on_off_en)
        if user.language == "es":
            try:
                text = text.replace("Выбранные горосокопы", "Horóscopos seleccionados")
                text = text.replace("Любовный,", "Amor")
                text = text.replace("Общий,", "General")
                text = text.replace("Деловой,", "Negocio")
                text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)",
                                    "No hay horóscopos seleccionados (no recibirán notificaciones)")
            except:
                pass
            await call.message.edit_text(f"{text}", reply_markup=on_off_es)
        if user.language == "de":
            try:
                text = text.replace("Выбранные горосокопы", "Ausgewählte Horoskope")
                text = text.replace("Любовный,", "Liebe")
                text = text.replace("Общий,", "Allgemein")
                text = text.replace("Деловой,", "Geschäft")
                text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)",
                                    "Es gibt keine ausgewählten Horoskope (Benachrichtigungen werden nicht kommen)")
            except:
                pass
            await call.message.edit_text(f"{text}", reply_markup=on_off_de)
    else:
        if user.language == "ru":
            await call.message.edit_text(f"Нет выбранных гороскопов (уведомления не будут приходить)", reply_markup=on_off_ru)
        if user.language == "en":
            await call.message.edit_text(f"There are no selected horoscopes (notifications will not come)", reply_markup=on_off_en)
        if user.language == "es":
            await call.message.edit_text(f"No hay horóscopos seleccionados (no recibirán notificaciones)", reply_markup=on_off_es)
        if user.language == "de":
            await call.message.edit_text(f"Es gibt keine ausgewählten Horoskope (Benachrichtigungen werden nicht kommen)", reply_markup=on_off_de)


@dp.callback_query_handler(text="on_off_business")
async def def_mame(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    if user.notify_horo:
        print("if 1")
        selected_horoscope = str(user.notify_horo)
        selected_horoscope_split = user.notify_horo.split()
        x = 0
        z = 0
        for y in selected_horoscope_split:
            z += 1
        for i in selected_horoscope_split:
            print("for i")
            if i == "Деловой,":
                print("if 2")
                text = str(selected_horoscope).replace("Деловой, ", "")
                await qc.update_selected_horo(id=int(call.from_user.id), text=text)
            else:
                x += 1
        if x >= z:
            print("else 2")
            text = selected_horoscope + "Деловой, "
            await qc.update_selected_horo(id=int(call.from_user.id), text=text)
    else:
        print("else 1")
        text = " Деловой, "
        await qc.update_selected_horo(id=call.from_user.id, text=text)
    user_upd = await qc.get_user(id=int(call.from_user.id))
    if user_upd.notify_horo:
        text = f"Выбранные горосокопы:\n" \
               f"\n" \
               f"{user_upd.notify_horo}"
        if user.language == "ru":
            await call.message.edit_text(f"{text}", reply_markup=on_off_ru)
        if user.language == "en":
            try:
                text = text.replace("Выбранные горосокопы", "Selected horoscopes")
                text = text.replace("Любовный,", "Love")
                text = text.replace("Общий,", "General")
                text = text.replace("Деловой,", "Business")
                text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)",
                                    "There are no selected horoscopes (notifications will not come)")
            except:
                pass
            await call.message.edit_text(f"{text}", reply_markup=on_off_en)
        if user.language == "es":
            try:
                text = text.replace("Выбранные горосокопы", "Horóscopos seleccionados")
                text = text.replace("Любовный,", "Amor")
                text = text.replace("Общий,", "General")
                text = text.replace("Деловой,", "Negocio")
                text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)",
                                    "No hay horóscopos seleccionados (no recibirán notificaciones)")
            except:
                pass
            await call.message.edit_text(f"{text}", reply_markup=on_off_es)
        if user.language == "de":
            try:
                text = text.replace("Выбранные горосокопы", "Ausgewählte Horoskope")
                text = text.replace("Любовный,", "Liebe")
                text = text.replace("Общий,", "Allgemein")
                text = text.replace("Деловой,", "Geschäft")
                text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)",
                                    "Es gibt keine ausgewählten Horoskope (Benachrichtigungen werden nicht kommen)")
            except:
                pass
            await call.message.edit_text(f"{text}", reply_markup=on_off_de)
    else:
        if user.language == "ru":
            await call.message.edit_text(f"Нет выбранных гороскопов (уведомления не будут приходить)",
                                         reply_markup=on_off_ru)
        if user.language == "en":
            await call.message.edit_text(f"There are no selected horoscopes (notifications will not come)",
                                         reply_markup=on_off_en)
        if user.language == "es":
            await call.message.edit_text(f"No hay horóscopos seleccionados (no recibirán notificaciones)",
                                         reply_markup=on_off_es)
        if user.language == "de":
            await call.message.edit_text(
                f"Es gibt keine ausgewählten Horoskope (Benachrichtigungen werden nicht kommen)",
                reply_markup=on_off_de)


@dp.callback_query_handler(text="on_off_regular")
async def def_mame(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    if user.notify_horo:
        print("if 1")
        selected_horoscope = str(user.notify_horo)
        selected_horoscope_split = user.notify_horo.split()
        x = 0
        z = 0
        for y in selected_horoscope_split:
            z += 1
        for i in selected_horoscope_split:
            print(i)
            if i == "Общий,":
                print("if 2")
                text = str(selected_horoscope).replace("Общий, ", "")
                await qc.update_selected_horo(id=int(call.from_user.id), text=text)
            else:
                x += 1
        if x >= z:
            print("else 2")
            text = selected_horoscope + "Общий, "
            await qc.update_selected_horo(id=int(call.from_user.id), text=text)
    else:
        print("else 1")
        text = "Общий, "
        await qc.update_selected_horo(id=call.from_user.id, text=text)
    user_upd = await qc.get_user(id=int(call.from_user.id))
    if user_upd.notify_horo:
        text = f"Выбранные горосокопы:\n" \
               f"\n" \
               f"{user_upd.notify_horo}"
        if user.language == "ru":
            await call.message.edit_text(f"{text}", reply_markup=on_off_ru)
        if user.language == "en":
            try:
                text = text.replace("Выбранные горосокопы", "Selected horoscopes")
                text = text.replace("Любовный,", "Love")
                text = text.replace("Общий,", "General")
                text = text.replace("Деловой,", "Business")
                text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)",
                                    "There are no selected horoscopes (notifications will not come)")
            except:
                pass
            await call.message.edit_text(f"{text}", reply_markup=on_off_en)
        if user.language == "es":
            try:
                text = text.replace("Выбранные горосокопы", "Horóscopos seleccionados")
                text = text.replace("Любовный,", "Amor")
                text = text.replace("Общий,", "General")
                text = text.replace("Деловой,", "Negocio")
                text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)",
                                    "No hay horóscopos seleccionados (no recibirán notificaciones)")
            except:
                pass
            await call.message.edit_text(f"{text}", reply_markup=on_off_es)
        if user.language == "de":
            try:
                text = text.replace("Выбранные горосокопы", "Ausgewählte Horoskope")
                text = text.replace("Любовный,", "Liebe")
                text = text.replace("Общий,", "Allgemein")
                text = text.replace("Деловой,", "Geschäft")
                text = text.replace("Нет выбранных гороскопов (уведомления не будут приходить)",
                                    "Es gibt keine ausgewählten Horoskope (Benachrichtigungen werden nicht kommen)")
            except:
                pass
            await call.message.edit_text(f"{text}", reply_markup=on_off_de)
    else:
        if user.language == "ru":
            await call.message.edit_text(f"Нет выбранных гороскопов (уведомления не будут приходить)",
                                         reply_markup=on_off_ru)
        if user.language == "en":
            await call.message.edit_text(f"There are no selected horoscopes (notifications will not come)",
                                         reply_markup=on_off_en)
        if user.language == "es":
            await call.message.edit_text(f"No hay horóscopos seleccionados (no recibirán notificaciones)",
                                         reply_markup=on_off_es)
        if user.language == "de":
            await call.message.edit_text(
                f"Es gibt keine ausgewählten Horoskope (Benachrichtigungen werden nicht kommen)",
                reply_markup=on_off_de)

@dp.callback_query_handler(text="edit_time_zone")
async def def_mame(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    if user.language == "ru":
        await call.message.edit_text(f"Ваш часовой пояс {user.time_zone}\n"
                                     f"\n"
                                     f"Выберите нужный часовой пояс", reply_markup=time_zone_kb)
        await Profile.time_zone.set()
    if user.language == "en":
        await call.message.edit_text(f"Your time zone {user.time_zone}\n"
                                     f"\n"
                                     f"Select the desired time zone", reply_markup=time_zone_kb)
        await Profile.time_zone.set()
    if user.language == "es":
        await call.message.edit_text(f"Tu zona horaria {user.time_zone}\n"
                                     f"\n"
                                     f"Seleccione la zona horaria deseada", reply_markup=time_zone_kb)
        await Profile.time_zone.set()
    if user.language == "de":
        await call.message.edit_text(f"Deine Zeitzone {user.time_zone}\n"
                                     f"\n"
                                     f"Wählen Sie die gewünschte Zeitzone", reply_markup=time_zone_kb)
        await Profile.time_zone.set()


@dp.callback_query_handler(Text(
    equals=["UTC-10", "UTC-9", "UTC-8", "UTC-7", "UTC-6", "UTC-5", "UTC-4", "UTC-3", "UTC-2", "UTC-1", "UTC-0",
            "UTC+12", "UTC+11", "UTC+10", "UTC+9",
            "UTC+8", "UTC+7", "UTC+6", "UTC+5", "UTC+4", "UTC+3", "UTC+2", "UTC+1"]), state=Profile.time_zone)
async def time_zone(call: types.CallbackQuery, state: FSMContext):
    time_zone = call.data
    user = await qc.get_user(id=int(call.from_user.id))
    if user.language == "ru":
        await call.message.edit_text(f"Ваш часовой пояс изменен на {time_zone}\n"
                                     f"\n"
                                     f"Не забудьте выбрать новое время для уведомлений (сейчас они отключены)",
                                     reply_markup=None)
    if user.language == "en":
        await call.message.edit_text(f"Your time zone has been changed to {time_zone}\n"
                                     f"\n"
                                     f"Don't forget to choose a new time for notifications (they are now disabled)",
                                     reply_markup=None)
    if user.language == "es":
        await call.message.edit_text(f"Tu zona horaria se ha cambiado a {time_zone}\n"
                                     f"\n"
                                     f"No olvide elegir una nueva hora para las notificaciones (ahora están deshabilitadas)",
                                     reply_markup=None)
    if user.language == "de":
        await call.message.edit_text(f"Ihre Zeitzone wurde geändert in {time_zone}\n"
                                     f"\n"
                                     f"Vergessen Sie nicht, eine neue Zeit für Benachrichtigungen auszuwählen (sie sind jetzt deaktiviert).",
                                     reply_markup=None)
    await qc.update_time_zone(id=int(call.from_user.id), time_zone=time_zone)
    await qc.update_notify_time(id=int(call.from_user.id), notify_time=None, moscow_time=None)
    await state.finish()


@dp.callback_query_handler(text="edit_time")
async def def_mame(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    time_zone = user.time_zone
    notify_time = user.notify_time
    if user.language == "ru":
        await call.message.edit_text(f"Ваш часовой пояс: {time_zone}\n"
                                     f"\n"
                                     f"Выберите время, в которое вы хотите получать уведомления",
                                     reply_markup=notify_time_kb)
    if user.language == "en":
        await call.message.edit_text(f"You will receive notifications at {notify_time}\n"
                                     f"\n"
                                     f"Select the time at which you want to receive notifications",
                                     reply_markup=notify_time_kb)
    if user.language == "es":
        await call.message.edit_text(f"Recibirás notificaciones las {notify_time}\n"
                                     f"\n"
                                     f"Seleccione la hora a la que desea recibir notificaciones",
                                     reply_markup=notify_time_kb)
    if user.language == "de":
        await call.message.edit_text(f"Sie erhalten Benachrichtigungen um {notify_time}\n"
                                     f"\n"
                                     f"Wählen Sie die Uhrzeit aus, zu der Sie Benachrichtigungen erhalten möchten",
                                     reply_markup=notify_time_kb)


@dp.callback_query_handler(Text(
    equals=["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00",
            "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00",
            "23:00"]))
async def def_mame(call: types.CallbackQuery):
    notify_time = call.data
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
        moscow_temp = int(hours[0])
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
    try:
        moscow_time = str(moscow_time).replace("-", "")
    except:
        print("Число и так положительное")
    await qc.update_notify_time(id=call.from_user.id, notify_time=notify_time, moscow_time=moscow_time)
    user = await qc.get_user(id=int(call.from_user.id))
    if user.language == "ru":
        await call.message.edit_text(f"Вам будут приходить уведомления в {notify_time}\n"
                                     f"\n"
                                     f"Что бы выбрать гороскопы - нажмите [изменить гороскопы]",
                                     reply_markup=edit_notify_time_kb_ru)
    if user.language == "en":
        await call.message.edit_text(f"You will receive notifications at {notify_time}\n"
                                     f"\n"
                                     f"To choose horoscopes - click [change horoscopes]",
                                     reply_markup=edit_notify_time_kb_en)
    if user.language == "es":
        await call.message.edit_text(f"Recibirás notificaciones las {notify_time}\n"
                                     f"\n"
                                     f"Para elegir horóscopos, haga clic en [cambiar horóscopos]",
                                     reply_markup=edit_notify_time_kb_es)
    if user.language == "de":
        await call.message.edit_text(f"Sie erhalten Benachrichtigungen um {notify_time}\n"
                                     f"\n"
                                     f"Um Horoskope auszuwählen - klicken Sie auf [Horoskope ändern]",
                                     reply_markup=edit_notify_time_kb_de)


@dp.message_handler(Text(equals=["Назад", "Back to", "De regreso", "zurück"]), state='*')
async def def_name(message: types.Message, state: FSMContext):
    user = await qc.get_user(id=int(message.from_user.id))
    if user.language == "ru":
        await message.answer(f"Вы возвращены в главное меню", reply_markup=menu_ru)
    if user.language == "en":
        await message.answer(f"You are returned to the main menu", reply_markup=menu_en)
    if user.language == "es":
        await message.answer(f"Vuelve al menú principal.", reply_markup=menu_es)
    if user.language == "de":
        await message.answer(f"Sie kehren zum Hauptmenü zurück\n",
                             reply_markup=menu_de)


@dp.message_handler(Text(
    equals=["Изменить дату и время рождения", "Change date and time of birth", "Cambiar fecha y hora de nacimiento",
            "Geburtsdatum und -uhrzeit ändern"]), state='*')
async def def_name(message: types.Message, state: FSMContext):
    user = await qc.get_user(id=int(message.from_user.id))
    if user.language == "ru":
        await message.answer(f"Текущае дата рождения: <b>{user.birthday.replace(' ', '.')}</b>\n"
                             f"Время рождения: <b>{user.time_birthday.replace(' ', ':')}</b>\n"
                             f"\n"
                             f"Введите дату вашего рождения\n"
                             f"<i>Например 21.04.1990</i>", reply_markup=None)
    if user.language == "en":
        await message.answer(f"Current date of birth: <b>{user.birthday.replace(' ', '.')}</b>\n"
                             f"Birth time: <b>{user.time_birthday}</b>\n"
                             f"\n"
                             f"Enter your date of birth\n"
                             f"<i>For example 21/04/1990</i>", reply_markup=None)
    if user.language == "es":
        await message.answer(f"Fecha de nacimiento actual: <b>{user.birthday.replace(' ', '.')}</b>\n"
                             f"Hora de nacimiento: <b>{user.time_birthday}</b>\n"
                             f"\n"
                             f"Introduzca su fecha de nacimiento\n"
                             f"<i>Por ejemplo 21/04/1990</i>", reply_markup=None)
    if user.language == "de":
        await message.answer(f"Aktuelles Geburtsdatum: <b>{user.birthday.replace(' ', '.')}</b>\n"
                             f"Geburtszeit: <b>{user.time_birthday}</b>\n"
                             f"\n"
                             f"Gib dein Geburtsdatum ein\n"
                             f"<i>Zum Beispiel 15.04.1990</i>", reply_markup=None)
    await Settings.birthday.set()


@dp.message_handler(state=Settings.birthday)
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
            if (int(date_split[0]) >= 21 and int(date_split[1]) == 1) or (
                    int(date_split[0]) <= 19 and int(date_split[1]) == 2):
                zodiac = "Aquarius"
            if (int(date_split[0]) >= 20 and int(date_split[1]) == 2) or (
                    int(date_split[0]) <= 20 and int(date_split[1]) == 3):
                zodiac = "Pisces"
            if (int(date_split[0]) >= 21 and int(date_split[1]) == 3) or (
                    int(date_split[0]) <= 20 and int(date_split[1]) == 4):
                zodiac = "Aries"
            if (int(date_split[0]) >= 21 and int(date_split[1]) == 4) or (
                    int(date_split[0]) <= 21 and int(date_split[1]) == 5):
                zodiac = "Taurus"
            if (int(date_split[0]) >= 22 and int(date_split[1]) == 5) or (
                    int(date_split[0]) <= 21 and int(date_split[1]) == 6):
                zodiac = "Gemini"
            if (int(date_split[0]) >= 22 and int(date_split[1]) == 6) or (
                    int(date_split[0]) <= 22 and int(date_split[1]) == 7):
                zodiac = "Cancer"
            if (int(date_split[0]) >= 23 and int(date_split[1]) == 7) or (
                    int(date_split[0]) <= 21 and int(date_split[1]) == 8):
                zodiac = "Leo"
            if (int(date_split[0]) >= 22 and int(date_split[1]) == 8) or (
                    int(date_split[0]) <= 23 and int(date_split[1]) == 9):
                zodiac = "Virgo"
            if (int(date_split[0]) >= 24 and int(date_split[1]) == 9) or (
                    int(date_split[0]) <= 23 and int(date_split[1]) == 10):
                zodiac = "Libra"
            if (int(date_split[0]) >= 24 and int(date_split[1]) == 10) or (
                    int(date_split[0]) <= 22 and int(date_split[1]) == 11):
                zodiac = "Scorpio"
            if (int(date_split[0]) >= 23 and int(date_split[1]) == 11) or (
                    int(date_split[0]) <= 22 and int(date_split[1]) == 12):
                zodiac = "Sagittarius"
            if (int(date_split[0]) >= 23 and int(date_split[1]) == 12) or (
                    int(date_split[0]) <= 20 and int(date_split[1]) == 1):
                zodiac = "Sagittarius"
            await qc.update_zodiac(id=int(message.from_user.id), zodiac=zodiac)
            await qc.update_birthday(id=int(message.from_user.id), birthday=date, birthday_day=f"{date_split[0]}",
                                     birthday_month=f"{date_split[1]}", birthday_year=f"{date_split[2]}")
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
            await Settings.time.set()
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


@dp.callback_query_handler(text="skip_time_register", state=Settings.time)
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    await qc.update_time_birthday(id=int(call.from_user.id), time_birthday="-")
    user = await qc.get_user(id=int(call.from_user.id))
    if user.language == "ru":
        await call.message.edit_text(f"Вы успешно изменили дату и время вашего рождения")
    if user.language == "en":
        await call.message.edit_text(f"You have successfully changed your date and time of birth")
    if user.language == "es":
        await call.message.edit_text(f"Ha cambiado correctamente su fecha y hora de nacimiento.")
    if user.language == "de":
        await call.message.edit_text(f"Sie haben Ihr Geburtsdatum und Ihre Geburtszeit erfolgreich geändert")
    await state.finish()


@dp.message_handler(state=Settings.time)
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
        if 0 >= int(date_split[0]) or 23 < int(date_split[0]) or 0 >= int(date_split[1]) or 59 < int(date_split[1]):
            print(date_split[0], date_split[1])
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
        else:
            user = await qc.get_user(id=int(message.from_user.id))
            await qc.update_time_birthday(id=int(message.from_user.id), time_birthday=date)
            if user.language == "ru":
                await message.answer(f"Вы успешно изменили дату и время вашего рождения")
            if user.language == "en":
                await message.answer(f"You have successfully changed your date and time of birth")
            if user.language == "es":
                await message.answer(f"Ha cambiado correctamente su fecha y hora de nacimiento.")
            if user.language == "de":
                await message.answer(f"Sie haben Ihr Geburtsdatum und Ihre Geburtszeit erfolgreich geändert")
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
