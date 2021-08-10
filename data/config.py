from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста


DB_USER = env.str("BD_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")

cookie_gif = "CgACAgIAAxkBAAIOz2DwmNp4L-tiDmsJdY_cih4riodvAAICDwACE8WBSyJtXdvD9XsiIAQ"
server_cookie = "CgACAgIAAxkBAAIEdGDzf-54o_1XJkhBzdfjskOl3xpbAAIvDwACU3SYS-AmoZh1Azv9IAQ"
local_gif = "CgACAgIAAxkBAAIOz2DwmNp4L-tiDmsJdY_cih4riodvAAICDwACE8WBSyJtXdvD9XsiIAQ"

pifagor_img = "AgACAgIAAxkBAAIYJ2DzhiMKB_RFfGNfyN4mDDQ4sN1vAAJ5szEbfJehS8Tu6fE8h-LHAQADAgADeAADIAQ"
server_pif = "AgACAgIAAxkBAAIEwWDzhCkAAUsrmrs7iUSQUUnie5-JEQACjbUxG1N0mEvGVLm4GbkQ9AEAAwIAA3gAAyAE"
local_img = "AgACAgIAAxkBAAIR_WDyCcpDwMxMS9bicR8-BIrmdh3MAAKTszEbE8WRS89t2mR-N7YTAQADAgADeAADIAQ"



POSTGRES_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
# POSTGRES_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"