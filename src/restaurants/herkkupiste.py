"""Herkkupiste menu"""

from datetime import date

from lounaat_info import fetch_from_lounaat
from model.restaurant import Restaurant

NAME = 'Herkkupiste'
URL = 'https://www.herkkupiste.fi/lounaslista.html'


def fetch() -> Restaurant:
    """Fetches the menu."""
    return Restaurant(
        name=NAME,
        url=URL,
        menu=fetch_from_lounaat('herkkupiste/turku', date.today())
    )


if __name__ == '__main__':
    print(fetch())
