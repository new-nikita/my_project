import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменная окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
URL = os.getenv("URL")






