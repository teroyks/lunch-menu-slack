"""Sodexo Auriga Business Center menu"""

from datetime import date

from lounaat_info import fetch_from_lounaat
from model.restaurant import Restaurant

NAME = 'Sodexo Auriga Business Center'
URL = 'https://www.sodexo.fi/ravintolat/ravintola-fiskarholmen-auriga-business-center'


def fetch() -> Restaurant:
    """Fetches the menu."""
    return Restaurant(
        name=NAME,
        url=URL,
        menu=fetch_from_lounaat(
            'sodexo-auriga-business-center/turku', date.today())
    )


if __name__ == '__main__':
    print(fetch())
