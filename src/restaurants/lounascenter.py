"""Lounascenter menu"""

from datetime import date

from lounaat_info import fetch_from_lounaat
from model.restaurant import Restaurant

NAME = 'Lounascenter'
URL = 'https://lounascenter.fi/lounasravintola/viikon-lounaslista/'


def fetch() -> Restaurant:
    """Fetches the menu."""
    return Restaurant(
        name=NAME,
        url=URL,
        menu=fetch_from_lounaat('lounascenter/turku', date.today())
    )


if __name__ == '__main__':
    print(fetch())
