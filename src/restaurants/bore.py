"""Bore Hostel menu"""

from datetime import date

from lounaat_info import fetch_from_lounaat
from model.restaurant import Restaurant

NAME = 'Bore'
URL = 'https://www.hostelbore.fi/lounas'


def fetch() -> Restaurant:
    """Fetches the menu."""
    return Restaurant(
        name=NAME,
        url=URL,
        menu=fetch_from_lounaat('laivahostel-ss-bore/turku', date.today())
    )


if __name__ == '__main__':
    print(fetch())
