"""Rantakerttu menu"""

from datetime import date

from lounaat_info import fetch_from_lounaat
from model.restaurant import Restaurant

NAME = 'Rantakerttu'
URL = 'https://www.rantakerttu.fi/lounas'


def fetch() -> Restaurant:
    """Fetches the menu."""
    return Restaurant(
        name=NAME,
        url=URL,
        menu=fetch_from_lounaat('rantakerttu/turku', date.today())
    )


if __name__ == '__main__':
    print(fetch())
