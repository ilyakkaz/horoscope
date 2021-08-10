import asyncio
import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text

from data.config import cookie_gif
from keyboards.inline.prdiction_kb import prediction_ru, prediction_en, prediction_es, prediction_de, check_ru, \
    check_de, check_es, check_en, delete_msg_ru, delete_msg_de, delete_msg_es, delete_msg_en, more_prediction_ru, \
    more_prediction_en, more_prediction_es, more_prediction_de
from utils.db_api import quick_commands as qc

from loader import dp


@dp.message_handler(Text(equals=["Предсказание", "Prediction", "Predicción", "Prognose"]), state="*")
async def select_horoscope(message: types.Message, state: FSMContext):
    user = await qc.get_user(id=int(message.from_user.id))
    if user.language == "ru":
        await message.answer(f"Получите свое предсказание на сегодня", reply_markup=prediction_ru)
    if user.language == "en":
        await message.answer(f"Get your prediction for today", reply_markup=prediction_en)
    if user.language == "es":
        await message.answer(f"Obtenga su predicción para hoy", reply_markup=prediction_es)
    if user.language == "de":
        await message.answer(f"Holen Sie sich Ihre Vorhersage für heute", reply_markup=prediction_de)
    await state.finish()


@dp.callback_query_handler(Text(equals=["Предсказание", "Prediction", "Predicción", "Prognose"]), state="*")
async def select_horoscope(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete_reply_markup()
    user = await qc.get_user(id=int(call.from_user.id))
    if user.language == "ru":
        await call.message.answer(f"Получите свое предсказание на сегодня", reply_markup=prediction_ru)
    if user.language == "en":
        await call.message.answer(f"Get your prediction for today", reply_markup=prediction_en)
    if user.language == "es":
        await call.message.answer(f"Obtenga su predicción para hoy", reply_markup=prediction_es)
    if user.language == "de":
        await call.message.answer(f"Holen Sie sich Ihre Vorhersage für heute", reply_markup=prediction_de)
    await state.finish()


@dp.callback_query_handler(Text(equals=["pred_share_ru", "pred_share_en", "pred_share_es", "pred_share_de"]), state="*")
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    user = await qc.get_user(id=int(call.from_user.id))
    referrals = await qc.select_referrals(id=call.from_user.id)
    text = f""
    x = 0
    for referal in referrals:
        x += 1
        text += f"{x}) {referal.fullname}\n"
    if user.language == "ru":
        await call.message.answer(f"Ваша ссылка для приглашения: ")
        await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}", reply_markup=check_ru)
    if user.language == "en":
        await call.message.answer(f"Your invitation link: ")
        await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}", reply_markup=check_en)
    if user.language == "es":
        await call.message.answer(f"Su enlace de invitación:")
        await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}", reply_markup=check_es)
    if user.language == "de":
        await call.message.answer(f"Ihr Einladungslink:")
        await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}", reply_markup=check_de)
    await state.finish()


@dp.callback_query_handler(Text(equals=["pred_get_ru", "pred_get_en", "pred_get_es", "pred_get_de"]), state="*")
async def def_mame(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    user = await qc.get_user(id=int(call.from_user.id))
    referrals = await qc.select_referrals(id=call.from_user.id)
    x = 0
    for i in referrals:
        x += 1
    if user.language == "ru":
        if x < 3:
            await call.message.answer(f"Для активации функции пригласите минимум 3 людей.\n"
                                      f"Ваша ссылка для приглашения: ")
            await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}",
                                      reply_markup=check_ru)
        else:
            if user.prediction < 3:
                print("RU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                num = random.randint(1, 8)
                prediction = await qc.get_prediction(id=num)
                msg = await call.message.answer_animation(animation=cookie_gif)
                await asyncio.sleep(3)
                await msg.delete()
                await call.message.answer(f"Предсказание на сегодня:\n"
                                          f"\n"
                                          f"{prediction.ru}", reply_markup=more_prediction_ru)
                new_pred = user.prediction + 1
                await qc.plus_prediction(id=call.from_user.id, prediction=new_pred)
            else:
                await call.message.answer(f"⚠️В день можно получить 3 предсказания\n"
                                          f"\n"
                                          f"Пожалуйста, подождите до завтра")
    if user.language == "en":
        if x < 3:
            await call.message.answer(f"To activate the function, invite at least 3 people.\n"
                                      f"Your invitation link: ")
            await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}",
                                      reply_markup=check_en)
        else:
            if user.prediction < 3:
                print("RU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                num = random.randint(1, 8)
                prediction = await qc.get_prediction(id=num)
                msg = await call.message.answer_animation(animation=cookie_gif)
                await asyncio.sleep(3)
                await msg.delete()
                await call.message.answer(f"Prediction for today:\n"
                                          f"\n"
                                          f"{prediction.en}", reply_markup=more_prediction_en)
                new_pred = user.prediction + 1
                await qc.plus_prediction(id=call.from_user.id, prediction=new_pred)
            else:
                await call.message.answer(f"⚠️You can get 3 predictions per day\n"
                                          f"\n"
                                          f"Please wait until tomorrow")
    if user.language == "es":
        if x < 3:
            await call.message.answer(f"Para activar la función, invite al menos a 3 personas.\n"
                                      f"Su enlace de invitación: ")
            await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}",
                                      reply_markup=check_es)
        else:
            if user.prediction < 3:
                print("RU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                num = random.randint(1, 8)
                prediction = await qc.get_prediction(id=num)
                msg = await call.message.answer_animation(animation=cookie_gif)
                await asyncio.sleep(3)
                await msg.delete()
                await call.message.answer(f"Predicción para hoy:\n"
                                          f"\n"
                                          f"{prediction.es}", reply_markup=more_prediction_es)
                new_pred = user.prediction + 1
                await qc.plus_prediction(id=call.from_user.id, prediction=new_pred)
            else:
                await call.message.answer(f"⚠️Puede obtener 3 predicciones por día\n"
                                          f"\n"
                                          f"Por favor espere hasta mañana")
    if user.language == "de":
        if x < 3:
            await call.message.answer(f"Um die Funktion zu aktivieren, laden Sie mindestens 3 Personen ein.\n"
                                      f"Ihr Einladungslink: ")
            await call.message.answer(f"https://t.me/horo_server_temp_bot?start={call.from_user.id}",
                                      reply_markup=check_de)
        else:
            if user.prediction < 3:
                print("RU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                num = random.randint(1, 8)
                prediction = await qc.get_prediction(id=num)
                msg = await call.message.answer_animation(animation=cookie_gif)
                await asyncio.sleep(3)
                await msg.delete()
                await call.message.answer(f"Vorhersage für heute:\n"
                                          f"\n"
                                          f"{prediction.de}", reply_markup=more_prediction_de)
                new_pred = user.prediction + 1
                await qc.plus_prediction(id=call.from_user.id, prediction=new_pred)
            else:
                await call.message.answer(f"⚠️Sie können 3 Vorhersagen pro Tag erhalten\n"
                                          f"\n"
                                          f"Bitte bis morgen warten")
    await state.finish()