"""Post a test message to Slack"""

import requests

from slack import post_menu
from model.restaurant import Restaurant

Response = requests.models.Response


def test_send_message():
    """Post a test message"""
    restaurant = Restaurant(name='test', menu='menu from integration test')
    res: Response = post_menu(restaurant)
    assert res.status_code == 200, 'Should be able to post to Slack'
