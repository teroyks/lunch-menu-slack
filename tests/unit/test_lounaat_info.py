"""Tests the lounaat_info helper function with a mock API and Herkkupiste data."""

from datetime import date
import responses

from helpers import MenuMsg as Msg
from lounaat_info import LOUNAAT_URL, fetch_from_lounaat

URL = 'foo'
FULL_URL = f'{LOUNAAT_URL}/{URL}'

day = date(2020, 3, 10)


@responses.activate
def test_invalid_status():
    """API returns status code 400."""
    responses.add(responses.GET, FULL_URL, status=404)

    res = fetch_from_lounaat(URL, day)
    assert res == Msg.URL_NOT_FOUND, 'Should return URL not found error'


@responses.activate
def test_invalid_content():
    """API returns content that parser cannot handle."""
    responses.add(responses.GET, FULL_URL, status=200,
                  body='<html><body>No menu</body></html>')

    res = fetch_from_lounaat(URL, day)
    assert res == Msg.MENU_NOT_FOUND, 'Should not be able to parse the menu.'
