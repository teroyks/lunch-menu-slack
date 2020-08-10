"""Test fetching the Mauno menu"""

from helpers import MenuMsg
from restaurants import paviljonki


def test_fetch():
    """Fetch restaurant info from Mauno"""
    result = paviljonki.fetch()
    assert 'Noutopöydästä' in result.menu, 'Should have found menu content.'
