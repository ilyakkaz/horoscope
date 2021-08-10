from datetime import datetime

import pytz
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text

from keyboards.inline.horoscope_kb import horoscope_en, horoscope_es, horoscope_de, horoscope_ru, \
    horoscope_all5_ru, horoscope_business5_ru, horoscope_love2_ru, horoscope_love3_ru, horoscope_love4_ru, \
    horoscope_love1_ru, horoscope_love5_ru, horoscope_business1_ru, horoscope_business2_ru, horoscope_business3_ru, \
    horoscope_business4_ru, horoscope_all1_ru, horoscope_all2_ru, horoscope_all3_ru, horoscope_all4_ru, \
    horoscope_love2_en, horoscope_love3_en, horoscope_love4_en, horoscope_love5_en, horoscope_love1_en, \
    horoscope_love2_es, horoscope_love3_es, horoscope_love4_es, horoscope_love5_es, horoscope_love1_es, \
    horoscope_love1_de, horoscope_love5_de, horoscope_love4_de, horoscope_love3_de, horoscope_love2_de, \
    horoscope_business1_en, horoscope_business1_es, horoscope_business1_de, horoscope_business5_en, \
    horoscope_business4_en, horoscope_business3_en, horoscope_business2_en, horoscope_business5_es, \
    horoscope_business4_es, horoscope_business3_es, horoscope_business2_es, horoscope_business5_de, \
    horoscope_business4_de, horoscope_business3_de, horoscope_business2_de, horoscope_all2_en, horoscope_all3_en, \
    horoscope_all4_en, horoscope_all5_en, horoscope_all1_en, horoscope_all1_es, horoscope_all1_de, horoscope_all3_es, \
    horoscope_all2_es, horoscope_all5_es, horoscope_all4_es, horoscope_all5_de, horoscope_all3_de, horoscope_all4_de, \
    horoscope_all2_de
from utils.db_api import quick_commands as qc

from loader import dp


@dp.callback_query_handler(text="delete_msg", state="*")
async def delete_msg(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()


@dp.message_handler(Text(equals=["Гороскоп", "Horoscope", "Horóscopo", "Horoskop"]), state="*")
async def select_horoscope(message: types.Message, state: FSMContext):
    user = await qc.get_user(id=int(message.from_user.id))
    if user.language == "ru":
        await message.answer(f"Какой гороскоп вы хотите увидеть?", reply_markup=horoscope_ru)
    if user.language == "en":
        await message.answer(f"What horoscope do you want to see?", reply_markup=horoscope_en)
    if user.language == "es":
        await message.answer(f"¿Qué horóscopo quieres ver?", reply_markup=horoscope_es)
    if user.language == "de":
        await message.answer(f"Welches Horoskop möchtest du sehen?", reply_markup=horoscope_de)
    await state.finish()


@dp.callback_query_handler(text="h_love")
async def love_horoscope(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    await call.message.delete()
    if user.language == "ru":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="ru", type="Любовный")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"💌Ваш любовный гороскоп на сегодня: \n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_love1_ru)
    if user.language == "en":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="en", type="Любовный")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"💌Your love horoscope for today:\n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_love1_en)
    if user.language == "es":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="es", type="Любовный")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"💌Tu horóscopo del amor para hoy:\n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_love1_es)
    if user.language == "de":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="de", type="Любовный")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"💌Ihr Liebeshoroskop für heute:\n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_love1_de)


@dp.callback_query_handler(text="h_business")
async def business_horoscope(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    await call.message.delete()
    if user.language == "ru":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="ru", type="Деловой")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"🗓Ваш деловой гороскоп на сегодня: \n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_business1_ru)
    if user.language == "en":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="en", type="Деловой")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"🗓Your business horoscope for today:\n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_business1_en)
    if user.language == "es":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="es", type="Деловой")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"🗓Tu horóscopo empresarial para hoy:\n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_business1_es)
    if user.language == "de":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="de", type="Деловой")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"🗓Ihr Geschäftshoroskop für heute:\n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_business1_de)


@dp.callback_query_handler(text="h_all")
async def all_horoscope(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    await call.message.delete()
    if user.language == "ru":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="ru", type="Общий")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"☀️Ваш общий гороскоп на сегодня: \n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_all1_ru)
    if user.language == "en":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="en", type="Общий")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"☀️Your overall horoscope for today:\n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_all1_en)
    if user.language == "es":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="es", type="Общий")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"☀️Tu horóscopo general para hoy:\n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_all1_es)
    if user.language == "de":
        now = datetime.now(pytz.timezone("europe/moscow"))
        date = now.strftime("%d,%m,%Y")
        horoscope = await qc.get_horoscope(date=date, language="de", type="Общий")
        zodiac = user.zodiac
        if zodiac == "Aries":
            text = horoscope.Aries
        if zodiac == "Taurus":
            text = horoscope.Taurus
        if zodiac == "Gemini":
            text = horoscope.Gemini
        if zodiac == "Cancer":
            text = horoscope.Cancer
        if zodiac == "Leo":
            text = horoscope.Leo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Virgo":
            text = horoscope.Virgo
        if zodiac == "Libra":
            text = horoscope.Libra
        if zodiac == "Scorpio":
            text = horoscope.Scorpio
        if zodiac == "Sagittarius":
            text = horoscope.Sagittarius
        if zodiac == "Capricorn":
            text = horoscope.Capricorn
        if zodiac == "Aquarius":
            text = horoscope.Aquarius
        if zodiac == "Pisces":
            text = horoscope.Pisces
        await call.message.answer(f"☀️Ihr Gesamthoroskop für heute:\n"
                                  f"\n"
                                  f"{text}", reply_markup=horoscope_all1_de)


@dp.callback_query_handler(Text(equals=["h_love5_1", "h_love5_2", "h_love5_3", "h_love5_4"]))
async def all_horoscope(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    how_many_days = call.data
    print("===================================================", how_many_days)
    await call.message.delete()
    if user.language == "ru":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_love5_1":
            date_d = int(now.strftime("%d"))+1
        if how_many_days == "h_love5_2":
            date_d = int(now.strftime("%d"))+2
        if how_many_days == "h_love5_3":
            date_d = int(now.strftime("%d"))+3
        if how_many_days == "h_love5_4":
            date_d = int(now.strftime("%d"))+4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="ru", type="Любовный")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="ru", type="Любовный")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="ru", type="Любовный")
                print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="ru", type="Любовный")
                print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_love5_1":
                date_d = 1
            if how_many_days == "h_love5_2":
                date_d = 2
            if how_many_days == "h_love5_3":
                date_d = 3
            if how_many_days == "h_love5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="ru", type="Любовный")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="ru", type="Любовный")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="ru", type="Любовный")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="ru", type="Любовный")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
                if zodiac == "Aries":
                    text += f"{horoscope.Aries}\n\n"
                if zodiac == "Taurus":
                    text += f"{horoscope.Taurus}\n\n"
                if zodiac == "Gemini":
                    text += f"{horoscope.Gemini}\n\n"
                if zodiac == "Cancer":
                    text += f"{horoscope.Cancer}\n\n"
                if zodiac == "Leo":
                    text += f"{horoscope.Leo}\n\n"
                if zodiac == "Virgo":
                    text += f"{horoscope.Virgo}\n\n"
                if zodiac == "Virgo":
                    text += f"{horoscope.Virgo}\n\n"
                if zodiac == "Libra":
                    text += f"{horoscope.Libra}\n\n"
                if zodiac == "Scorpio":
                    text += f"{horoscope.Scorpio}\n\n"
                if zodiac == "Sagittarius":
                    text += f"{horoscope.Sagittarius}\n\n"
                if zodiac == "Capricorn":
                    text += f"{horoscope.Capricorn}\n\n"
                if zodiac == "Aquarius":
                    text += f"{horoscope.Aquarius}\n\n"
                if zodiac == "Pisces":
                    text += f"{horoscope.Pisces}\n\n"
        except:
                print("нет такой даты в таблице")
        if how_many_days == "h_love5_1":
            await call.message.answer(f"💌Ваш любовный гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love2_ru)
        if how_many_days == "h_love5_2":
            await call.message.answer(f"💌Ваш любовный гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love3_ru)
        if how_many_days == "h_love5_3":
            await call.message.answer(f"💌Ваш любовный гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love4_ru)
        if how_many_days == "h_love5_4":
            await call.message.answer(f"💌Ваш любовный гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love5_ru)
    if user.language == "en":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_love5_1":
            date_d = int(now.strftime("%d"))+1
        if how_many_days == "h_love5_2":
            date_d = int(now.strftime("%d"))+2
        if how_many_days == "h_love5_3":
            date_d = int(now.strftime("%d"))+3
        if how_many_days == "h_love5_4":
            date_d = int(now.strftime("%d"))+4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="en", type="Любовный")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="en", type="Любовный")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="en", type="Любовный")
                print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="en", type="Любовный")
                print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_love5_1":
                date_d = 1
            if how_many_days == "h_love5_2":
                date_d = 2
            if how_many_days == "h_love5_3":
                date_d = 3
            if how_many_days == "h_love5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="en", type="Любовный")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="en", type="Любовный")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="en", type="Любовный")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="en", type="Любовный")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
                if zodiac == "Aries":
                    text += f"{horoscope.Aries}\n\n"
                if zodiac == "Taurus":
                    text += f"{horoscope.Taurus}\n\n"
                if zodiac == "Gemini":
                    text += f"{horoscope.Gemini}\n\n"
                if zodiac == "Cancer":
                    text += f"{horoscope.Cancer}\n\n"
                if zodiac == "Leo":
                    text += f"{horoscope.Leo}\n\n"
                if zodiac == "Virgo":
                    text += f"{horoscope.Virgo}\n\n"
                if zodiac == "Virgo":
                    text += f"{horoscope.Virgo}\n\n"
                if zodiac == "Libra":
                    text += f"{horoscope.Libra}\n\n"
                if zodiac == "Scorpio":
                    text += f"{horoscope.Scorpio}\n\n"
                if zodiac == "Sagittarius":
                    text += f"{horoscope.Sagittarius}\n\n"
                if zodiac == "Capricorn":
                    text += f"{horoscope.Capricorn}\n\n"
                if zodiac == "Aquarius":
                    text += f"{horoscope.Aquarius}\n\n"
                if zodiac == "Pisces":
                    text += f"{horoscope.Pisces}\n\n"
        except:
                print("нет такой даты в таблице")
        if how_many_days == "h_love5_1":
            await call.message.answer(f"Your love horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love2_en)
        if how_many_days == "h_love5_2":
            await call.message.answer(f"Your love horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love3_en)
        if how_many_days == "h_love5_3":
            await call.message.answer(f"Your love horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love4_en)
        if how_many_days == "h_love5_4":
            await call.message.answer(f"Your love horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love5_en)
    if user.language == "es":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_love5_1":
            date_d = int(now.strftime("%d")) + 1
        if how_many_days == "h_love5_2":
            date_d = int(now.strftime("%d")) + 2
        if how_many_days == "h_love5_3":
            date_d = int(now.strftime("%d")) + 3
        if how_many_days == "h_love5_4":
            date_d = int(now.strftime("%d")) + 4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="es", type="Любовный")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="es", type="Любовный")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="es", type="Любовный")
            print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="es", type="Любовный")
            print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_love5_1":
                date_d = 1
            if how_many_days == "h_love5_2":
                date_d = 2
            if how_many_days == "h_love5_3":
                date_d = 3
            if how_many_days == "h_love5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="es", type="Любовный")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="es", type="Любовный")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="es", type="Любовный")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="es", type="Любовный")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
            if zodiac == "Aries":
                text += f"{horoscope.Aries}\n\n"
            if zodiac == "Taurus":
                text += f"{horoscope.Taurus}\n\n"
            if zodiac == "Gemini":
                text += f"{horoscope.Gemini}\n\n"
            if zodiac == "Cancer":
                text += f"{horoscope.Cancer}\n\n"
            if zodiac == "Leo":
                text += f"{horoscope.Leo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Libra":
                text += f"{horoscope.Libra}\n\n"
            if zodiac == "Scorpio":
                text += f"{horoscope.Scorpio}\n\n"
            if zodiac == "Sagittarius":
                text += f"{horoscope.Sagittarius}\n\n"
            if zodiac == "Capricorn":
                text += f"{horoscope.Capricorn}\n\n"
            if zodiac == "Aquarius":
                text += f"{horoscope.Aquarius}\n\n"
            if zodiac == "Pisces":
                text += f"{horoscope.Pisces}\n\n"
        except:
            print("нет такой даты в таблице")
        if how_many_days == "h_love5_1":
            await call.message.answer(f"Tu horóscopo del amor es el {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love2_es)
        if how_many_days == "h_love5_2":
            await call.message.answer(f"Tu horóscopo del amor es el {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love3_es)
        if how_many_days == "h_love5_3":
            await call.message.answer(f"Tu horóscopo del amor es el {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love4_es)
        if how_many_days == "h_love5_4":
            await call.message.answer(f"Tu horóscopo del amor es el {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love5_es)
    if user.language == "de":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_love5_1":
            date_d = int(now.strftime("%d")) + 1
        if how_many_days == "h_love5_2":
            date_d = int(now.strftime("%d")) + 2
        if how_many_days == "h_love5_3":
            date_d = int(now.strftime("%d")) + 3
        if how_many_days == "h_love5_4":
            date_d = int(now.strftime("%d")) + 4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="de", type="Любовный")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="de", type="Любовный")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="de", type="Любовный")
            print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="de", type="Любовный")
            print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_love5_1":
                date_d = 1
            if how_many_days == "h_love5_2":
                date_d = 2
            if how_many_days == "h_love5_3":
                date_d = 3
            if how_many_days == "h_love5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="de", type="Любовный")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="de", type="Любовный")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="de", type="Любовный")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="de", type="Любовный")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
            if zodiac == "Aries":
                text += f"{horoscope.Aries}\n\n"
            if zodiac == "Taurus":
                text += f"{horoscope.Taurus}\n\n"
            if zodiac == "Gemini":
                text += f"{horoscope.Gemini}\n\n"
            if zodiac == "Cancer":
                text += f"{horoscope.Cancer}\n\n"
            if zodiac == "Leo":
                text += f"{horoscope.Leo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Libra":
                text += f"{horoscope.Libra}\n\n"
            if zodiac == "Scorpio":
                text += f"{horoscope.Scorpio}\n\n"
            if zodiac == "Sagittarius":
                text += f"{horoscope.Sagittarius}\n\n"
            if zodiac == "Capricorn":
                text += f"{horoscope.Capricorn}\n\n"
            if zodiac == "Aquarius":
                text += f"{horoscope.Aquarius}\n\n"
            if zodiac == "Pisces":
                text += f"{horoscope.Pisces}\n\n"
        except:
            print("нет такой даты в таблице")
        if how_many_days == "h_love5_1":
            await call.message.answer(f"Dein Liebeshoroskop ist das {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love2_de)
        if how_many_days == "h_love5_2":
            await call.message.answer(f"Dein Liebeshoroskop ist das {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love3_de)
        if how_many_days == "h_love5_3":
            await call.message.answer(f"Dein Liebeshoroskop ist das {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love4_de)
        if how_many_days == "h_love5_4":
            await call.message.answer(f"Dein Liebeshoroskop ist das {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_love5_de)


@dp.callback_query_handler(Text(equals=["h_business5_1", "h_business5_2", "h_business5_3", "h_business5_4"]))
async def all_horoscope(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    how_many_days = call.data
    print("===================================================", how_many_days)
    await call.message.delete()
    if user.language == "ru":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_business5_1":
            date_d = int(now.strftime("%d")) + 1
        if how_many_days == "h_business5_2":
            date_d = int(now.strftime("%d")) + 2
        if how_many_days == "h_business5_3":
            date_d = int(now.strftime("%d")) + 3
        if how_many_days == "h_business5_4":
            date_d = int(now.strftime("%d")) + 4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="ru", type="Деловой")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="ru", type="Деловой")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="ru", type="Деловой")
            print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="ru", type="Деловой")
            print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_business5_1":
                date_d = 1
            if how_many_days == "h_business5_2":
                date_d = 2
            if how_many_days == "h_business5_3":
                date_d = 3
            if how_many_days == "h_business5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="ru", type="Деловой")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="ru", type="Деловой")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="ru", type="Деловой")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="ru", type="Деловой")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
            if zodiac == "Aries":
                text += f"{horoscope.Aries}\n\n"
            if zodiac == "Taurus":
                text += f"{horoscope.Taurus}\n\n"
            if zodiac == "Gemini":
                text += f"{horoscope.Gemini}\n\n"
            if zodiac == "Cancer":
                text += f"{horoscope.Cancer}\n\n"
            if zodiac == "Leo":
                text += f"{horoscope.Leo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Libra":
                text += f"{horoscope.Libra}\n\n"
            if zodiac == "Scorpio":
                text += f"{horoscope.Scorpio}\n\n"
            if zodiac == "Sagittarius":
                text += f"{horoscope.Sagittarius}\n\n"
            if zodiac == "Capricorn":
                text += f"{horoscope.Capricorn}\n\n"
            if zodiac == "Aquarius":
                text += f"{horoscope.Aquarius}\n\n"
            if zodiac == "Pisces":
                text += f"{horoscope.Pisces}\n\n"
        except:
            print("нет такой даты в таблице")
        if how_many_days == "h_business5_1":
            await call.message.answer(f"🗓Ваш деловой гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business2_ru)
        if how_many_days == "h_business5_2":
            await call.message.answer(f"🗓Ваш деловой гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business3_ru)
        if how_many_days == "h_business5_3":
            await call.message.answer(f"🗓Ваш деловой гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business4_ru)
        if how_many_days == "h_business5_4":
            await call.message.answer(f"🗓Ваш деловой гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business5_ru)
    if user.language == "en":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_business5_1":
            date_d = int(now.strftime("%d")) + 1
        if how_many_days == "h_business5_2":
            date_d = int(now.strftime("%d")) + 2
        if how_many_days == "h_business5_3":
            date_d = int(now.strftime("%d")) + 3
        if how_many_days == "h_business5_4":
            date_d = int(now.strftime("%d")) + 4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="en", type="Деловой")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="en", type="Деловой")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="en", type="Деловой")
            print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="en", type="Деловой")
            print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_business5_1":
                date_d = 1
            if how_many_days == "h_business5_2":
                date_d = 2
            if how_many_days == "h_business5_3":
                date_d = 3
            if how_many_days == "h_business5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="en", type="Деловой")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="en", type="Деловой")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="en", type="Деловой")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="en", type="Деловой")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
            if zodiac == "Aries":
                text += f"{horoscope.Aries}\n\n"
            if zodiac == "Taurus":
                text += f"{horoscope.Taurus}\n\n"
            if zodiac == "Gemini":
                text += f"{horoscope.Gemini}\n\n"
            if zodiac == "Cancer":
                text += f"{horoscope.Cancer}\n\n"
            if zodiac == "Leo":
                text += f"{horoscope.Leo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Libra":
                text += f"{horoscope.Libra}\n\n"
            if zodiac == "Scorpio":
                text += f"{horoscope.Scorpio}\n\n"
            if zodiac == "Sagittarius":
                text += f"{horoscope.Sagittarius}\n\n"
            if zodiac == "Capricorn":
                text += f"{horoscope.Capricorn}\n\n"
            if zodiac == "Aquarius":
                text += f"{horoscope.Aquarius}\n\n"
            if zodiac == "Pisces":
                text += f"{horoscope.Pisces}\n\n"
        except:
            print("нет такой даты в таблице")
        if how_many_days == "h_business5_1":
            await call.message.answer(f"Your business horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business2_en)
        if how_many_days == "h_business5_2":
            await call.message.answer(f"Your business horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business3_en)
        if how_many_days == "h_business5_3":
            await call.message.answer(f"Your business horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business4_en)
        if how_many_days == "h_business5_4":
            await call.message.answer(f"Your business horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business5_en)
    if user.language == "es":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_business5_1":
            date_d = int(now.strftime("%d")) + 1
        if how_many_days == "h_business5_2":
            date_d = int(now.strftime("%d")) + 2
        if how_many_days == "h_business5_3":
            date_d = int(now.strftime("%d")) + 3
        if how_many_days == "h_business5_4":
            date_d = int(now.strftime("%d")) + 4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="es", type="Деловой")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="es", type="Деловой")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="es", type="Деловой")
            print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="es", type="Деловой")
            print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_business5_1":
                date_d = 1
            if how_many_days == "h_business5_2":
                date_d = 2
            if how_many_days == "h_business5_3":
                date_d = 3
            if how_many_days == "h_business5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="es", type="Деловой")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="es", type="Деловой")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="es", type="Деловой")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="es", type="Деловой")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
            if zodiac == "Aries":
                text += f"{horoscope.Aries}\n\n"
            if zodiac == "Taurus":
                text += f"{horoscope.Taurus}\n\n"
            if zodiac == "Gemini":
                text += f"{horoscope.Gemini}\n\n"
            if zodiac == "Cancer":
                text += f"{horoscope.Cancer}\n\n"
            if zodiac == "Leo":
                text += f"{horoscope.Leo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Libra":
                text += f"{horoscope.Libra}\n\n"
            if zodiac == "Scorpio":
                text += f"{horoscope.Scorpio}\n\n"
            if zodiac == "Sagittarius":
                text += f"{horoscope.Sagittarius}\n\n"
            if zodiac == "Capricorn":
                text += f"{horoscope.Capricorn}\n\n"
            if zodiac == "Aquarius":
                text += f"{horoscope.Aquarius}\n\n"
            if zodiac == "Pisces":
                text += f"{horoscope.Pisces}\n\n"
        except:
            print("нет такой даты в таблице")
        if how_many_days == "h_business5_1":
            await call.message.answer(f"Tu horóscopo empresarial para {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business2_es)
        if how_many_days == "h_business5_2":
            await call.message.answer(f"Tu horóscopo empresarial para {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business3_es)
        if how_many_days == "h_business5_3":
            await call.message.answer(f"Tu horóscopo empresarial para {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business4_es)
        if how_many_days == "h_business5_4":
            await call.message.answer(f"Tu horóscopo empresarial para {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business5_es)
    if user.language == "de":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_business5_1":
            date_d = int(now.strftime("%d")) + 1
        if how_many_days == "h_business5_2":
            date_d = int(now.strftime("%d")) + 2
        if how_many_days == "h_business5_3":
            date_d = int(now.strftime("%d")) + 3
        if how_many_days == "h_business5_4":
            date_d = int(now.strftime("%d")) + 4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="de", type="Деловой")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="de", type="Деловой")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="de", type="Деловой")
            print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="de", type="Деловой")
            print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_business5_1":
                date_d = 1
            if how_many_days == "h_business5_2":
                date_d = 2
            if how_many_days == "h_business5_3":
                date_d = 3
            if how_many_days == "h_business5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="de", type="Деловой")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="de", type="Деловой")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="de", type="Деловой")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="de", type="Деловой")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
            if zodiac == "Aries":
                text += f"{horoscope.Aries}\n\n"
            if zodiac == "Taurus":
                text += f"{horoscope.Taurus}\n\n"
            if zodiac == "Gemini":
                text += f"{horoscope.Gemini}\n\n"
            if zodiac == "Cancer":
                text += f"{horoscope.Cancer}\n\n"
            if zodiac == "Leo":
                text += f"{horoscope.Leo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Libra":
                text += f"{horoscope.Libra}\n\n"
            if zodiac == "Scorpio":
                text += f"{horoscope.Scorpio}\n\n"
            if zodiac == "Sagittarius":
                text += f"{horoscope.Sagittarius}\n\n"
            if zodiac == "Capricorn":
                text += f"{horoscope.Capricorn}\n\n"
            if zodiac == "Aquarius":
                text += f"{horoscope.Aquarius}\n\n"
            if zodiac == "Pisces":
                text += f"{horoscope.Pisces}\n\n"
        except:
            print("нет такой даты в таблице")
        if how_many_days == "h_business5_1":
            await call.message.answer(f"Ihr Geschäftshoroskop ist auf {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business2_de)
        if how_many_days == "h_business5_2":
            await call.message.answer(f"Ihr Geschäftshoroskop ist auf {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business3_de)
        if how_many_days == "h_business5_3":
            await call.message.answer(f"Ihr Geschäftshoroskop ist auf {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business4_de)
        if how_many_days == "h_business5_4":
            await call.message.answer(f"Ihr Geschäftshoroskop ist auf {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_business5_de)


@dp.callback_query_handler(Text(equals=["h_all5_1", "h_all5_2", "h_all5_3", "h_all5_4"]))
async def all_horoscope(call: types.CallbackQuery):
    user = await qc.get_user(id=int(call.from_user.id))
    how_many_days = call.data
    print("===================================================", how_many_days)
    await call.message.delete()
    if user.language == "ru":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_all5_1":
            date_d = int(now.strftime("%d")) + 1
        if how_many_days == "h_all5_2":
            date_d = int(now.strftime("%d")) + 2
        if how_many_days == "h_all5_3":
            date_d = int(now.strftime("%d")) + 3
        if how_many_days == "h_all5_4":
            date_d = int(now.strftime("%d")) + 4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="ru", type="Общий")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="ru", type="Общий")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="ru", type="Общий")
            print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="ru", type="Общий")
            print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_all5_1":
                date_d = 1
            if how_many_days == "h_all5_2":
                date_d = 2
            if how_many_days == "h_all5_3":
                date_d = 3
            if how_many_days == "h_all5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="ru", type="Общий")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="ru", type="Общий")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="ru", type="Общий")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="ru", type="Общий")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
            if zodiac == "Aries":
                text += f"{horoscope.Aries}\n\n"
            if zodiac == "Taurus":
                text += f"{horoscope.Taurus}\n\n"
            if zodiac == "Gemini":
                text += f"{horoscope.Gemini}\n\n"
            if zodiac == "Cancer":
                text += f"{horoscope.Cancer}\n\n"
            if zodiac == "Leo":
                text += f"{horoscope.Leo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Libra":
                text += f"{horoscope.Libra}\n\n"
            if zodiac == "Scorpio":
                text += f"{horoscope.Scorpio}\n\n"
            if zodiac == "Sagittarius":
                text += f"{horoscope.Sagittarius}\n\n"
            if zodiac == "Capricorn":
                text += f"{horoscope.Capricorn}\n\n"
            if zodiac == "Aquarius":
                text += f"{horoscope.Aquarius}\n\n"
            if zodiac == "Pisces":
                text += f"{horoscope.Pisces}\n\n"
        except:
            print("нет такой даты в таблице")
        if how_many_days == "h_all5_1":
            await call.message.answer(f"☀️Ваш общий гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all2_ru)
        if how_many_days == "h_all5_2":
            await call.message.answer(f"☀️Ваш общий гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all3_ru)
        if how_many_days == "h_all5_3":
            await call.message.answer(f"☀️Ваш общий гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all4_ru)
        if how_many_days == "h_all5_4":
            await call.message.answer(f"☀️Ваш общий гороскоп на {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all5_ru)
    if user.language == "en":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_all5_1":
            date_d = int(now.strftime("%d")) + 1
        if how_many_days == "h_all5_2":
            date_d = int(now.strftime("%d")) + 2
        if how_many_days == "h_all5_3":
            date_d = int(now.strftime("%d")) + 3
        if how_many_days == "h_all5_4":
            date_d = int(now.strftime("%d")) + 4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="en", type="Общий")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="en", type="Общий")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="en", type="Общий")
            print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="en", type="Общий")
            print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_all5_1":
                date_d = 1
            if how_many_days == "h_all5_2":
                date_d = 2
            if how_many_days == "h_all5_3":
                date_d = 3
            if how_many_days == "h_all5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="en", type="Общий")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="en", type="Общий")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="en", type="Общий")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="en", type="Общий")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
            if zodiac == "Aries":
                text += f"{horoscope.Aries}\n\n"
            if zodiac == "Taurus":
                text += f"{horoscope.Taurus}\n\n"
            if zodiac == "Gemini":
                text += f"{horoscope.Gemini}\n\n"
            if zodiac == "Cancer":
                text += f"{horoscope.Cancer}\n\n"
            if zodiac == "Leo":
                text += f"{horoscope.Leo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Libra":
                text += f"{horoscope.Libra}\n\n"
            if zodiac == "Scorpio":
                text += f"{horoscope.Scorpio}\n\n"
            if zodiac == "Sagittarius":
                text += f"{horoscope.Sagittarius}\n\n"
            if zodiac == "Capricorn":
                text += f"{horoscope.Capricorn}\n\n"
            if zodiac == "Aquarius":
                text += f"{horoscope.Aquarius}\n\n"
            if zodiac == "Pisces":
                text += f"{horoscope.Pisces}\n\n"
        except:
            print("нет такой даты в таблице")
        if how_many_days == "h_all5_1":
            await call.message.answer(f"Your general horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all2_en)
        if how_many_days == "h_all5_2":
            await call.message.answer(f"Your general horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all3_en)
        if how_many_days == "h_all5_3":
            await call.message.answer(f"Your general horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all4_en)
        if how_many_days == "h_all5_4":
            await call.message.answer(f"Your general horoscope for {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all5_en)
    if user.language == "es":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_all5_1":
            date_d = int(now.strftime("%d")) + 1
        if how_many_days == "h_all5_2":
            date_d = int(now.strftime("%d")) + 2
        if how_many_days == "h_all5_3":
            date_d = int(now.strftime("%d")) + 3
        if how_many_days == "h_all5_4":
            date_d = int(now.strftime("%d")) + 4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="es", type="Общий")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="es", type="Общий")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="es", type="Общий")
            print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="es", type="Общий")
            print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_all5_1":
                date_d = 1
            if how_many_days == "h_all5_2":
                date_d = 2
            if how_many_days == "h_all5_3":
                date_d = 3
            if how_many_days == "h_all5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="es", type="Общий")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="es", type="Общий")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="es", type="Общий")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="es", type="Общий")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
            if zodiac == "Aries":
                text += f"{horoscope.Aries}\n\n"
            if zodiac == "Taurus":
                text += f"{horoscope.Taurus}\n\n"
            if zodiac == "Gemini":
                text += f"{horoscope.Gemini}\n\n"
            if zodiac == "Cancer":
                text += f"{horoscope.Cancer}\n\n"
            if zodiac == "Leo":
                text += f"{horoscope.Leo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Libra":
                text += f"{horoscope.Libra}\n\n"
            if zodiac == "Scorpio":
                text += f"{horoscope.Scorpio}\n\n"
            if zodiac == "Sagittarius":
                text += f"{horoscope.Sagittarius}\n\n"
            if zodiac == "Capricorn":
                text += f"{horoscope.Capricorn}\n\n"
            if zodiac == "Aquarius":
                text += f"{horoscope.Aquarius}\n\n"
            if zodiac == "Pisces":
                text += f"{horoscope.Pisces}\n\n"
        except:
            print("нет такой даты в таблице")
        if how_many_days == "h_all5_1":
            await call.message.answer(f"Tu horóscopo general para {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all2_es)
        if how_many_days == "h_all5_2":
            await call.message.answer(f"Tu horóscopo general para {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all3_es)
        if how_many_days == "h_all5_3":
            await call.message.answer(f"Tu horóscopo general para {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all4_es)
        if how_many_days == "h_all5_4":
            await call.message.answer(f"Tu horóscopo general para {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all5_es)
    if user.language == "de":
        now = datetime.now(pytz.timezone("europe/moscow"))
        if how_many_days == "h_all5_1":
            date_d = int(now.strftime("%d")) + 1
        if how_many_days == "h_all5_2":
            date_d = int(now.strftime("%d")) + 2
        if how_many_days == "h_all5_3":
            date_d = int(now.strftime("%d")) + 3
        if how_many_days == "h_all5_4":
            date_d = int(now.strftime("%d")) + 4
        date_m = int(now.strftime("%m"))
        date_y = now.strftime("%Y")
        text = ""
        print(f"{date_d},{date_m},{date_y}")
        horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="de", type="Общий")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="de", type="Общий")
            print(f"{date_d},0{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="de", type="Общий")
            print(f"0{date_d},{date_m},{date_y}")
        if horoscope is None:
            horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="de", type="Общий")
            print(f"0{date_d},0{date_m},{date_y}")
        print(horoscope)
        if horoscope is None:
            if how_many_days == "h_all5_1":
                date_d = 1
            if how_many_days == "h_all5_2":
                date_d = 2
            if how_many_days == "h_all5_3":
                date_d = 3
            if how_many_days == "h_all5_4":
                date_d = 4
            date_m += 1
            horoscope = await qc.get_horoscope(date=f"{date_d},{date_m},{date_y}", language="de", type="Общий")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"{date_d},0{date_m},{date_y}", language="de", type="Общий")
                print(f"{date_d},0{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},{date_m},{date_y}", language="de", type="Общий")
                print(f"0{date_d},{date_m},{date_y}")
            if horoscope is None:
                horoscope = await qc.get_horoscope(date=f"0{date_d},0{date_m},{date_y}", language="de", type="Общий")
                print(f"0{date_d},0{date_m},{date_y}")
        zodiac = user.zodiac
        try:
            if zodiac == "Aries":
                text += f"{horoscope.Aries}\n\n"
            if zodiac == "Taurus":
                text += f"{horoscope.Taurus}\n\n"
            if zodiac == "Gemini":
                text += f"{horoscope.Gemini}\n\n"
            if zodiac == "Cancer":
                text += f"{horoscope.Cancer}\n\n"
            if zodiac == "Leo":
                text += f"{horoscope.Leo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Virgo":
                text += f"{horoscope.Virgo}\n\n"
            if zodiac == "Libra":
                text += f"{horoscope.Libra}\n\n"
            if zodiac == "Scorpio":
                text += f"{horoscope.Scorpio}\n\n"
            if zodiac == "Sagittarius":
                text += f"{horoscope.Sagittarius}\n\n"
            if zodiac == "Capricorn":
                text += f"{horoscope.Capricorn}\n\n"
            if zodiac == "Aquarius":
                text += f"{horoscope.Aquarius}\n\n"
            if zodiac == "Pisces":
                text += f"{horoscope.Pisces}\n\n"
        except:
            print("нет такой даты в таблице")
        if how_many_days == "h_all5_1":
            await call.message.answer(f"Ihr allgemeines Horoskop für {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all2_de)
        if how_many_days == "h_all5_2":
            await call.message.answer(f"Ihr allgemeines Horoskop für {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all3_de)
        if how_many_days == "h_all5_3":
            await call.message.answer(f"Ihr allgemeines Horoskop für {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all4_de)
        if how_many_days == "h_all5_4":
            await call.message.answer(f"Ihr allgemeines Horoskop für {date_d}.{date_m}.{date_y}: \n"
                                      f"\n"
                                      f"{text}", reply_markup=horoscope_all5_de)