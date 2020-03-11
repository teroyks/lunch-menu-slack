"""Hus Lindman menu"""

from datetime import date

from lounaat_info import fetch_from_lounaat
from model.restaurant import Restaurant

NAME = 'Hus Lindman'
URL = 'https://huli.fi/lounas-turku'


def fetch() -> Restaurant:
    """Fetches the menu."""
    return Restaurant(
        name=NAME,
        url=URL,
        menu=fetch_from_lounaat('hus-lindman/turku', date.today())
    )


if __name__ == '__main__':
    print(fetch())
