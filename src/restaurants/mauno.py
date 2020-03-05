"""Mauno Trivium menu"""

from datetime import date
import re
import requests

from bs4 import BeautifulSoup, SoupStrainer
from sspipe import p

from helpers import MenuMsg as Msg
from model.restaurant import Restaurant

NAME = 'Mauno Trivium'
URL = 'https://www.mauno.fi/fi/lounaslistat'


def _parse_menu_cards(html_content) -> list:
    """Parse today's menu cards for all Mauno restaurants."""
    today = date.today().isoformat()
    only_div_tags = SoupStrainer('div')

    soup = BeautifulSoup(html_content, 'html.parser', parse_only=only_div_tags)

    try:
        column = soup.find(attrs={'data-date': today})
        return column.select('div.menu-card')
    except AttributeError:
        return []


def _is_trivium(card) -> bool:
    """Checks if this is the restaurant we want."""
    heading = card.find('h3')
    return heading and heading.get_text() == 'TriviumCity'


def _trim_indentation(string: str) -> str:
    return re.sub(r' {4,}', '- ', string)


def _emphasize_subheadings(string: str) -> str:
    return re.sub(r'(.*buffet.*)', r'\n*\1*', string, flags=re.IGNORECASE)


def _parse_menu(menu: str) -> str:
    parsed_menu = (
        menu.split('\n')
        | p(map, lambda x: x.rstrip())
        | p(map, _trim_indentation)
        | p(filter, lambda x: x != '')
        | p(map, _emphasize_subheadings)
        | p(list)
        | p('\n'.join)
    )

    # combine prices with previous line
    return re.sub(r'\n\-', ' –', parsed_menu)


def _fetch_menu(url) -> str:
    """Fetches today's menu"""
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        return Msg.URL_NOT_FOUND

    if response.status_code != 200:
        return Msg.URL_NOT_FOUND

    cards = _parse_menu_cards(response.text)

    trivium_menu = [card.get_text() for card in cards if _is_trivium(card)]
    menu_str = '\n'.join(trivium_menu)

    return _parse_menu(menu_str)


def fetch() -> Restaurant:
    """Fetches the menu."""
    return Restaurant(
        name=NAME,
        url=URL,
        menu=_fetch_menu(URL)
    )


if __name__ == '__main__':
    print(fetch())

    # pylint: disable=line-too-long
    # raw_menu = '\n\nTriviumCity\n\n\n\n\n                                Lemminkäisenkatu 32, 20520 Turku\n                            \n\n\n\n\n\nLounas tarjoillaan klo 11-13\n\n\n\n\n\n\n\n\nBuffet\nMaunon pannupihvit, tummaa sipulikastiketta, perunamuusia ja kasviksia L,G\n                                                    \n                                                    \n\n\n                                                    10,70 €                                                \n\n\n\nSalaattibuffet\nKokoa mieleisesi annos\n                                                    \n                                                    \n\n\n                                                    9,50 €                                                \n\n\n\n \nKaikkiin lounaisiin kuuluu kahvi/tee ja jälkiruoka\n                                                    \n                                                    \n\n\n\n\n\n'
    # print(_parse_menu(raw_menu))
    # print(re.sub(r'\n', r'\\n', _parse_menu(raw_menu)))
