from datetime import datetime

import pytz
from aiogram import Dispatcher, types

from loader import bot, dp
from utils.db_api import quick_commands as qc


async def horoscope_00(dp: Dispatcher):
    await qc.set_zero_prediction()
    all_users = await qc.horoscope_notify(moscow_time1="00:00", moscow_time2="0:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"💌Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")

                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"🗓Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"☀️Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_01(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="01:00", moscow_time2="1:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")

                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_02(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="02:00", moscow_time2="2:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_03(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="03:00", moscow_time2="3:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_04(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="04:00", moscow_time2="4:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_05(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="05:00", moscow_time2="5:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_06(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="06:00", moscow_time2="6:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_07(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="07:00", moscow_time2="7:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_08(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="08:00", moscow_time2="8:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_09(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="09:00", moscow_time2="9:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_10(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="10:00", moscow_time2="10:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_11(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="11:00", moscow_time2="11:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_12(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="12:00", moscow_time2="12:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_13(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="13:00", moscow_time2="13:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_14(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="14:00", moscow_time2="14:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_15(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="15:00", moscow_time2="15:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_16(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="16:00", moscow_time2="16:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_17(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="17:00", moscow_time2="17:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_18(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="18:00", moscow_time2="18:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_19(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="19:00", moscow_time2="19:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_20(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="20:00", moscow_time2="20:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_21(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="21:00", moscow_time2="21:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_22(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="22:00", moscow_time2="22:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass


async def horoscope_23(dp: Dispatcher):
    all_users = await qc.horoscope_notify(moscow_time1="23:00", moscow_time2="23:00")
    print(all_users)
    for user in all_users:
        try:
            notify_horo = user.notify_horo
            notify_horo = notify_horo.split()
            love = 0
            business = 0
            regular = 0
            for i in notify_horo:
                if i == "Любовный,":
                    love = 1
                if i == "Деловой,":
                    business = 1
                if i == "Общий,":
                    regular = 1
            if user.language == "ru":
                now = datetime.now(pytz.timezone("europe/moscow"))
                date = now.strftime("%d,%m,%Y")
                if love == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш любовный гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if business == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш деловой гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if regular == 1:
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
                    await bot.send_message(chat_id=user.id, text=f"Ваш общий гороскоп на {date}: \n"
                                                                 f"\n"
                                                                 f"{text}")
                if user.first_notify == "yes":
                    await bot.send_message(chat_id=user.id, text=f"💡Каждый день, в это время, вам будет приходить ваш гороскоп\n"
                                                                 f"\n"
                                                                 f"Что бы изменить время уведомлений или отключить их - перейдите в Профиль -> Уведомления")
                    await qc.first_notify_off(id=user.id)
        except:
            pass
