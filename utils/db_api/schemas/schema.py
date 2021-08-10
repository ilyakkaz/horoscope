from sqlalchemy import Float, Column, BigInteger, String, sql, Integer

from utils.db_api.db_gino import TimedBaseModel


class Users(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    fullname = Column(String(255))
    username = Column(String(255))
    language = Column(String(20))
    time_zone = Column(String(50))
    birthday = Column(String(20))
    birthday_day = Column(String(20))
    birthday_month = Column(String(20))
    birthday_year = Column(String(20))
    time_birthday = Column(String(20))
    sex = Column(String(10))
    referral = Column(BigInteger)
    notify_time = Column(String(10))
    zodiac = Column(String(25))
    moscow_time = Column(String(10))
    prediction = Column(Integer)
    notify_horo = Column(String(255))
    first_notify = Column(String(10))




    query: sql.Select


class Horoscope(TimedBaseModel):
    __tablename__ = 'horoscope'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    language = Column(String(10))
    date = Column(String(255))
    type = Column(String(255))
    Aries = Column(String)
    Taurus = Column(String)
    Gemini = Column(String)
    Cancer = Column(String)
    Leo = Column(String)
    Virgo = Column(String)
    Libra = Column(String)
    Scorpio = Column(String)
    Sagittarius = Column(String)
    Capricorn = Column(String)
    Aquarius = Column(String)
    Pisces = Column(String)


    query: sql.Select


class Prediction(TimedBaseModel):
    __tablename__ = 'prediction'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    ru = Column(String)
    en = Column(String)
    es = Column(String)
    de = Column(String)


    query: sql.Select