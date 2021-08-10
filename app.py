from aiogram import executor

from handlers.users.sheduler import horoscope_00, horoscope_23, horoscope_22, horoscope_21, horoscope_20, horoscope_19, \
    horoscope_18, horoscope_17, horoscope_16, horoscope_15, horoscope_14, horoscope_13, horoscope_12, horoscope_11, \
    horoscope_10, horoscope_09, horoscope_08, horoscope_07, horoscope_06, horoscope_05, horoscope_04, horoscope_03, \
    horoscope_02, horoscope_01
from loader import dp, scheduler
import middlewares, filters, handlers
from utils.db_api import db_gino
from utils.db_api.db_gino import db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

def scheduler_job00():
    scheduler.add_job(horoscope_00, "cron", day_of_week='*', hour=00, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job01():
    scheduler.add_job(horoscope_01, "cron", day_of_week='*', hour=1, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job02():
    scheduler.add_job(horoscope_02, "cron", day_of_week='*', hour=2, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job03():
    scheduler.add_job(horoscope_03, "cron", day_of_week='*', hour=3, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job04():
    scheduler.add_job(horoscope_04, "cron", day_of_week='*', hour=4, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job05():
    scheduler.add_job(horoscope_05, "cron", day_of_week='*', hour=5, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job06():
    scheduler.add_job(horoscope_06, "cron", day_of_week='*', hour=6, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job07():
    scheduler.add_job(horoscope_07, "cron", day_of_week='*', hour=7, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job08():
    scheduler.add_job(horoscope_08, "cron", day_of_week='*', hour=8, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job09():
    scheduler.add_job(horoscope_09, "cron", day_of_week='*', hour=9, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job10():
    scheduler.add_job(horoscope_10, "cron", day_of_week='*', hour=10, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job11():
    scheduler.add_job(horoscope_11, "cron", day_of_week='*', hour=11, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job12():
    scheduler.add_job(horoscope_12, "cron", day_of_week='*', hour=12, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job13():
    scheduler.add_job(horoscope_13, "cron", day_of_week='*', hour=13, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job14():
    scheduler.add_job(horoscope_14, "cron", day_of_week='*', hour=14, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job15():
    scheduler.add_job(horoscope_15, "cron", day_of_week='*', hour=15, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job16():
    scheduler.add_job(horoscope_16, "cron", day_of_week='*', hour=16, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job17():
    scheduler.add_job(horoscope_17, "cron", day_of_week='*', hour=17, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job18():
    scheduler.add_job(horoscope_18, "cron", day_of_week='*', hour=18, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job19():
    scheduler.add_job(horoscope_19, "cron", day_of_week='*', hour=19, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job20():
    scheduler.add_job(horoscope_20, "cron", day_of_week='*', hour=20, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job21():
    scheduler.add_job(horoscope_21, "cron", day_of_week='*', hour=21, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job22():
    scheduler.add_job(horoscope_22, "cron", day_of_week='*', hour=22, minute=00, end_date='2024-05-30', args=(dp,))
def scheduler_job23():
    scheduler.add_job(horoscope_23, "cron", day_of_week='*', hour=23, minute=00, end_date='2024-05-30', args=(dp,))




async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    await db_gino.on_startup(dp)
    await db.gino.create_all()
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    scheduler_job00()
    scheduler_job01()
    scheduler_job02()
    scheduler_job03()
    scheduler_job04()
    scheduler_job05()
    scheduler_job06()
    scheduler_job07()
    scheduler_job08()
    scheduler_job09()
    scheduler_job10()
    scheduler_job11()
    scheduler_job12()
    scheduler_job13()
    scheduler_job14()
    scheduler_job15()
    scheduler_job16()
    scheduler_job17()
    scheduler_job18()
    scheduler_job19()
    scheduler_job20()
    scheduler_job21()
    scheduler_job22()
    scheduler_job23()


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
