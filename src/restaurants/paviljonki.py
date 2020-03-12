"""Kupittaan Paviljonki menu"""

from datetime import date
import re

from lounaat_info import fetch_from_lounaat
from model.restaurant import Restaurant

NAME = 'Kupittaan Paviljonki'
URL = 'https://www.kupittaanpaviljonki.fi/'


def _format(menu: str) -> str:
    return re.sub(r'(Noutopöytä|Pöytään.*)\n', r'*\1*\n', menu)


def fetch() -> Restaurant:
    """Fetches the menu."""
    return Restaurant(
        name=NAME,
        url=URL,
        menu=_format(fetch_from_lounaat(
            'kupittaan-paviljonki/turku', date.today()))
    )


if __name__ == '__main__':
    print(fetch())
