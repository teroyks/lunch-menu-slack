"""Test fetching the Mauno menu"""

from helpers import MenuMsg
from restaurants import mauno


def test_fetch():
    """Fetch restaurant info from Mauno"""
    result = mauno.fetch()
    assert 'TriviumCity' in result.menu, 'Should have found menu content.'


def test_url_not_found():
    """Try fetching from a nonexistent server."""
    # pylint: disable=protected-access
    menu = mauno._fetch_menu('')
    assert menu == MenuMsg.URL_NOT_FOUND
