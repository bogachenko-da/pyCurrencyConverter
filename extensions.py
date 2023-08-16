import requests
import json
from config import curr_keys


class APIException(Exception):
    """
    Базовый класс для представления исключений. Родитель: Exception.
    """
    pass


class Converter:
    """
    Класс для представления исключений, если пользователь вводит неверные данные.
    """
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        """
        Метод обрабатывает данные введенные пользователем, отправляет запрос к API,
        если данные введены неверны вызвает исключения.

        :param quote: str - исходная валюта
        :param base: str - имя валюты, в которою необходимо конвертировать
        :param amount: str - количество исходной валюты
        :return: float
        """
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = curr_keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = curr_keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[curr_keys[base]]
        return total_base * amount
