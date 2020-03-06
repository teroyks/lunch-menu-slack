"""Fetches today's menu for a restaurant in the Lounaat.info list."""

from datetime import date
import re
import requests

from bs4 import BeautifulSoup
from sspipe import p

from helpers import MenuMsg as Msg

LOUNAAT_URL = 'https://www.lounaat.info/lounas'


def _format_dishes(dishes: list) -> list:
    return (
        dishes
        | p(map, lambda x: x.get_text())
        | p(map, lambda x: re.sub(r'\s{2,}', r'  ', x))
        | p(list)
    )


def _parse_items(items: list, day: date) -> str:
    day_str = day.strftime('%-d.%-m.')

    for item in items:
        heading = item.find('h3')
        if heading and day_str in heading.get_text():
            dishes = item.select('p.dish')
            return '\n'.join([heading.get_text()] + _format_dishes(dishes))

    # item for given day not found
    return ''


def fetch_from_lounaat(restaurant_name: str, day: date) -> str:
    """Fetches today's menu for given restaurant.

    Args:
        restaurant_name: URL path for the restaurant, e.f. "foodbar/turku"
        day: Date for the menu

    Returns:
        Day's menu as a multi-line string

    """
    try:
        response = requests.get(f'{LOUNAAT_URL}/{restaurant_name}')
        response.encoding = 'utf-8'
    except requests.exceptions.RequestException:
        return Msg.URL_NOT_FOUND

    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', {'class': 'item'})

    return _parse_items(items, day) or Msg.MENU_NOT_FOUND


if __name__ == '__main__':
    print(fetch_from_lounaat('herkkupiste/turku', date.today()))
