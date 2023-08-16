import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

TOKEN = os.getenv('TOKEN')

curr_keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB',
}

DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку по командам бота"),
    ('values', "Вывести доступные валюты"),
)


