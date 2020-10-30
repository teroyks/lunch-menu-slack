"""Test fetching the Mauno menu"""

from helpers import MenuMsg
from restaurants import rantakerttu


def test_fetch():
    """Fetch restaurant info from Mauno"""
    result = rantakerttu.fetch()
    assert 'Rantakerttu' in result.name

    menu = result.menu.strip()
    assert menu, 'Should return some menu content.'
    assert not menu == MenuMsg.URL_NOT_FOUND, 'Should have been able to fetch the menu.'
    assert not menu == MenuMsg.MENU_NOT_FOUND, 'Should have parsed the menu content.'
