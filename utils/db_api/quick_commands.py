from asyncpg import UniqueViolationError

from aiogram import types, Bot
from gino import Gino
from sqlalchemy import and_, or_

db = Gino()

from utils.db_api.schemas.schema import Users, Horoscope, Prediction


'''функции для админки'''


async def select_all_users():
    users = await Users.query.gino.all()
    return users


async def count_users():
    total = await db.func.count(Users.id).gino.scalar()
    return total


async def count_users_sex(sex):
    total_sex = await Users.query.where(Users.sex == sex).gino.all()
    x = 0
    for i in total_sex:
        x += 1
    return x


async def count_users_language(language):
    total_language = await Users.query.where(Users.language == language).gino.all()
    x = 0
    for i in total_language:
        x += 1
    return x


async def get_users_language(language):
    total_language = await Users.query.where(Users.language == language).gino.all()
    return total_language


async def get_users_language_and_sex(language, sex):
    total_language = await Users.query.where(and_(Users.language == language, Users.sex == sex)).gino.all()
    return total_language


async def get_users_language_and_age_after(language, sex, year):
    total_language = await Users.query.where(and_(Users.language == language, Users.sex == sex, Users.birthday_year >= year)).gino.all()
    return total_language


async def get_users_language_and_age_after_no_sex(language, year):
    total_language = await Users.query.where(and_(Users.language == language, Users.birthday_year >= year)).gino.all()
    return total_language


async def get_users_language_and_date_and_sex(language, sex, day, month):
    total_language = await Users.query.where(and_(Users.language == language, Users.sex == sex, Users.birthday_day == day, Users.birthday_month == month)).gino.all()
    return total_language


async def get_users_language_date_no_sex(language, day, month):
    total_language = await Users.query.where(and_(Users.language == language, Users.birthday_day == day, Users.birthday_month == month)).gino.all()
    return total_language


async def get_users_language_and_age_before(language, sex, year):
    total_language = await Users.query.where(and_(Users.language == language, Users.sex == sex, Users.birthday_year <= year)).gino.all()
    return total_language


async def get_users_language_and_age_before_no_sex(language, year):
    total_language = await Users.query.where(and_(Users.language == language, Users.birthday_year <= year)).gino.all()
    return total_language


async def get_users_language_and_age_select(language, sex, year):
    total_language = await Users.query.where(and_(Users.language == language, Users.sex == sex, Users.birthday_year == year)).gino.all()
    return total_language


async def get_users_language_and_age_select_no_sex(language, year):
    total_language = await Users.query.where(and_(Users.language == language, Users.birthday_year == year)).gino.all()
    return total_language


async def count_users_sex_language(sex, language):
    total_sex = await Users.query.where(and_(Users.sex == sex, Users.language == language)).gino.all()
    x = 0
    for i in total_sex:
        x += 1
    return x


async def count_users_referrers():
    referrers = await Users.query.where(Users.referral != 0).gino.all()
    x = 0
    for i in referrers:
        x += 1
    return x


'''остальные функции'''


async def add_horoscope(date, language, type, Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces):
    try:
        # Users(user_id=user_id, user_name=user_name, telegram_id=telegram_id, balance=balance, orders=orders, language=language, orders_history=orders_history)
        horoscope = Horoscope(date=date, language=language, type=type, Aries=Aries, Taurus=Taurus, Gemini=Gemini, Cancer=Cancer, Leo=Leo, Virgo=Virgo
                              , Libra=Libra, Scorpio=Scorpio, Sagittarius=Sagittarius, Capricorn=Capricorn, Aquarius=Aquarius, Pisces=Pisces)
        await horoscope.create()
    except UniqueViolationError:
        pass


async def add_prediction(id, ru, en, es, de):
    try:
        # Users(user_id=user_id, user_name=user_name, telegram_id=telegram_id, balance=balance, orders=orders, language=language, orders_history=orders_history)
        prediction = Prediction(id=id, ru=ru, en=en, es=es, de=de)
        await prediction.create()
    except UniqueViolationError:
        pass


async def get_horoscope(date, language, type):
    horoscope = await Horoscope.query.where(and_(Horoscope.date == date, Horoscope.language == language, Horoscope.type == type)).gino.first()
    return horoscope


async def add_user(id, fullname, username, language, time_zone, birthday, time_birthday, sex, referral, notify_time, prediction):
    try:
        # Users(user_id=user_id, user_name=user_name, telegram_id=telegram_id, balance=balance, orders=orders, language=language, orders_history=orders_history)
        user = Users(id=id, fullname=fullname, username=username, language=language, time_zone=time_zone,
                     birthday=birthday, time_birthday=time_birthday, sex=sex, referral=referral, notify_time=notify_time, prediction=prediction)
        await user.create()
    except UniqueViolationError:
        pass
        # user = Users(id=id)
        # await user.update(fullname=fullname, username=username, language=language, time_zone=time_zone,
        #                   birthday=birthday, sex=sex).apply()


async def get_user(id: int):
    user = await Users.query.where(Users.id == id).gino.first()
    return user


async def update_user_balance(user_id, balance, orders, orders_history):
    user = await Users.get(user_id)
    await user.update(balance=balance, orders=orders, orders_history=orders_history).apply()


async def update_language(id, language):
    user = await Users.get(id)
    await user.update(language=language).apply()


async def update_time_zone(id, time_zone):
    user = await Users.get(id)
    await user.update(time_zone=time_zone).apply()


async def update_birthday(id, birthday, birthday_day, birthday_month, birthday_year):
    user = await Users.get(id)
    await user.update(birthday=birthday, birthday_day=birthday_day, birthday_month=birthday_month, birthday_year=birthday_year).apply()


async def update_time_birthday(id, time_birthday):
    user = await Users.get(id)
    await user.update(time_birthday=time_birthday).apply()


async def update_sex(id, sex, notify_time, moscow_time, notify_horo):
    user = await Users.get(id)
    await user.update(sex=sex, notify_time=notify_time, moscow_time=moscow_time, notify_horo=notify_horo, first_notify="yes").apply()


async def first_notify_off(id):
    user = await Users.get(id)
    await user.update(first_notify="no").apply()


async def update_zodiac(id, zodiac):
    user = await Users.get(id)
    await user.update(zodiac=zodiac).apply()
# async def select_all_users():
#     users = await Users.query.where(Users.user_id != 0).gino.all()
#     return users


async def select_referrals(id):
    users = await Users.query.where(Users.referral == id).gino.all()
    return users


async def drop_horoscope():
    await Horoscope.delete.where(Horoscope.id >= 0).gino.status()


async def drop_prediction():
    await Prediction.delete.where(Prediction.id >= 0).gino.status()


async def get_prediction(id):
    prediction = await Prediction.query.where(Prediction.id == id).gino.first()
    return prediction


async def update_notify_time(id, notify_time, moscow_time):
    user = await Users.get(id)
    await user.update(notify_time=notify_time, moscow_time=moscow_time).apply()


async def horoscope_notify(moscow_time1, moscow_time2):
    users = await Users.query.where(or_(Users.moscow_time == moscow_time1, Users.moscow_time == moscow_time2)).gino.all()
    return users


async def update_selected_horo(id, text):
    user = await Users.get(id)
    await user.update(notify_horo=text).apply()


async def plus_prediction(id, prediction):
    user = await Users.get(id)
    await user.update(prediction=prediction).apply()


async def set_zero_prediction():
    users = await Users.query.where(Users.prediction != 0).gino.all()
    for user in users:
        await user.update(prediction=0).apply()
# async def count_items_in_category(serves: str, category: str):
#     count_in_category = await Items.query.where(and_(Items.serves == serves, Items.category == category)).gino.scalar()
#     return count_in_category
#
#
# async def select_all_users():
#     users = await Users.query.gino.all()
#     return users
#
#
#
#
# async def count_users():
#     total = await db.func.count(Users.id).gino.scalar()
#     return total
#
#
# async def lk(id):
#     referrals = await Users.query.where(and_(Users.referral == id, Users.from_skammer == "No")).gino.all()
#     user = await Users.get(id)
#     num = len(referrals)
#     spend_rub = user.invest_rub
#     spend_btc = user.invest_btc
#     total = 0
#     for referral in referrals:
#         total += referral.invest_rub
#     text = (f"Вы обменяли {spend_rub} RUB\n"
#             f"Вы обменяли {spend_btc} BTC\n"
#             f"\n"
#             f"У вас {num} рефералов\n"
#             f"Они принесли вам {total * 0.008} руб")
#     return text
#
#
# async def total_white_balance(id):
#     referrals = await Users.query.where(and_(Users.referral == id, Users.from_skammer == "No")).gino.all()
#     total = 0
#     for referral in referrals:
#         total += referral.invest_rub
#     return total
#
#
# async def all_refs_white(id):
#     referrals = await Users.query.where(and_(Users.referral == id, Users.from_skammer == "No")).gino.all()
#     text = ""
#     num = 0
#     dict_id = {}
#     for x in referrals:
#         print(x)
#         num += 1
#         text += text.join([
#             f"{num})  <i>{x.name}</i>\n"
#             f"<b>{x.invest_rub * 0.008}</b> ₽, <b>{x.invest_btc * 0.008}</b> ₿\n"
#         ])
#     if text == "":
#         text = "У вас нет рефералов"
#     return text
#
#
# async def total_skam_balance(id):
#     referrals = await Users.query.where(and_(Users.referral == id, Users.from_skammer == "Yes")).gino.all()
#     total = 0
#     for referral in referrals:
#         total += referral.invest_rub
#     return total
#
#
# async def all_refs_skam(id):
#     referrals = await Users.query.where(and_(Users.referral == id, Users.from_skammer == "Yes")).gino.all()
#     text = ""
#     num = 0
#     dict_id = {}
#     for x in referrals:
#         print(x)
#         num += 1
#         if x.invest_rub != 0:
#             text += text.join([
#                 f"{num})  <i>{x.name}</i>\n"
#                 f"✅ <b>{x.invest_rub * 0.5}</b> ₽, <b>{x.invest_btc * 0.5}</b> ₿\n"
#                 f"\n"
#             ])
#         if x.invest_rub == 0:
#             text += text.join([
#                 f"{num})  <i>{x.name}</i>\n"
#                 f"🔘 <b>{x.invest_rub * 0.5}</b> ₽, <b>{x.invest_btc * 0.5}</b> ₿\n"
#                 f"\n"
#             ])
#     if text == "":
#         text = "У вас нет рефералов"
#     return text
#
#
# async def skam_lk(id):
#     referrals = await Users.query.where(and_(Users.referral == id,
#                                              Users.from_skammer == "Yes")).gino.all()
#     user = await Users.get(id)
#     num = len(referrals)
#     spend_rub = user.invest_rub
#     spend_btc = user.invest_btc
#     total = 0
#     for referral in referrals:
#         total += referral.invest_rub
#     text = (f"👨‍👦У вас рефералов: {num}\n"
#             f"\n"
#             f"💳Баланс на вывод:\n"
#             f"{total * 0.5} руб\n"
#             f"0.0 BTC\n"
#             f"\n"
#             f"")
#     return text
#
#
# async def check_referrals(id):
#     referrals = await Users.query.where(Users.referral == id).gino.all()
#     num = len(referrals)
#     total = 0
#     for referral in referrals:
#         total += referral.invest_rub
#     text = f"У вас {num} рефералов, они принесли вам {total} руб"
#     return text
#
#
# async def update_user_invest_rub(id, invest_rub, last):
#     user = await Users.get(id)
#     await user.update(invest_rub=invest_rub, last_invest_rub=last).apply()
#
#
# async def update_user_invest_btc(id, invest_btc):
#     user = await Users.get(id)
#     await user.update(invest_btc=invest_btc).apply()
