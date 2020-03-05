"""Test Mauno functions with mock API"""

import responses

from helpers import MenuMsg as Msg
from restaurants import mauno


@responses.activate
def test_invalid_status():
    """API returns status code 400"""
    responses.add(responses.GET, mauno.URL, status=400)

    res = mauno.fetch()
    assert res.menu == Msg.URL_NOT_FOUND, 'Should return URL not found error.'


@responses.activate
def test_invalid_content():
    """API returns content that parser cannot handle"""
    responses.add(responses.GET, mauno.URL, status=200,
                  body='<html><body>Nothing here</body></html>')

    res = mauno.fetch()
    assert res.menu == Msg.MENU_NOT_FOUND, 'Should not be able to parse the menu.'
