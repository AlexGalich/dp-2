import sys
from loguru import logger

from api.schemas import Games
from credentials import PUBLIC_KEY, SECRET_KEY


logger_config = {
    "handlers": [
        {"sink": sys.stderr, 'colorize': True, 'level': 'INFO'},
        # {"sink": "log/debug.log", "serialize": False, 'level': 'DEBUG'},
        {"sink": "log/info.log", "serialize": False, 'level': 'INFO'},
    ]
}
logger.configure(**logger_config)


API_URL = "https://api.dmarket.com"
API_URL_TRADING = API_URL
# GAMES = [Games.CS, Games.DOTA, Games.RUST]
GAMES = [Games.CS]
DATABASE_NAME = '/skins.db'

BAD_ITEMS = ['graffiti']


class Timers:
    PREV_BASE = 60 * 60 * 2
    ORDERS_BASE = 60 * 10


class PrevParams:
    # POPULARITY = 3
    MIN_AVG_PRICE = 900
    MAX_AVG_PRICE = 35000


class BuyParams:
    STOP_ORDERS_BALANCE = 1000
    FREQUENCY = True
    MIN_PRICE = 450
    MAX_PRICE = 10000

    PROFIT_PERCENT = 7
    GOOD_POINTS_PERCENT = 30
    AVG_PRICE_COUNT = 7

    ALL_SALES = 70
    DAYS_COUNT = 7
    SALE_COUNT = 10
    LAST_SALE = 1  # Последняя продажа не позднее LAST_SALE дней назад
    FIRST_SALE = 5  # Первая покупка не позже FIRST_SALE дней назад

    MAX_COUNT_SELL_OFFERS = 250

    BOOST_PERCENT = 24
    BOOST_POINTS = 3

    MAX_THRESHOLD = 3  # Максимальное повышение цены на MAX_THRESHOLD процентов от текущего ордера
    MIN_THRESHOLD = 3  # Максимальное понижение цены на MIN_THRESHOLD процентов от текущего ордера


class SellParams:
    MIN_PERCENT = 7
    MAX_PERCENT = 30
