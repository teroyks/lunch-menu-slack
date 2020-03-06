"""Test Mauno functions with mock API"""

import os
import pickle
import responses

from helpers import MenuMsg as Msg
from model.restaurant import Restaurant
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


@responses.activate
def test_parse_fixture():
    """Fetch menu info from a cached real data"""
    fixture_dir = os.path.dirname(os.path.realpath(__file__)) + '/fixtures'

    with open(fixture_dir + '/mauno.response', 'rb') as fixture:
        cached = pickle.load(fixture)
        responses.add(responses.GET, mauno.URL,
                      status=cached.status_code, body=cached.text)

    restaurant = mauno.fetch()
    assert isinstance(restaurant, Restaurant)
    assert restaurant.name == 'Mauno Trivium', 'Should return a result.'
    assert restaurant.url == mauno.URL

    assert isinstance(restaurant.menu, str)
    expected_string = 'TriviumCity – Lemminkäisenkatu 32, 20520 Turku'
    assert expected_string in restaurant.menu
