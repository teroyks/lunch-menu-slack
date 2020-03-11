"""Post a restaurant menu to Slack"""

import os
import requests

from model.restaurant import Restaurant

Response = requests.models.Response

URL = os.environ.get('SLACK_URL')


def post_to_url(url: str):
    """Creates a function that posts to API URL"""
    def post_params(*args, **kwargs) -> Response:
        # print('Posting', args, kwargs)
        return requests.post(url, *args, **kwargs)

    return post_params


def dummy_post(*_, **__) -> Response:
    """Dummy version for testing; does not post anything to outside APIs."""
    dummy_res = Response()
    dummy_res.status_code = 200
    dummy_res.code = 'ok'

    return dummy_res


post_to_api = post_to_url(URL) if URL else dummy_post


def build_query_payload(data: Restaurant) -> dict:
    """Builds Slack payload

    Args:
        data (Restaurant): Restaurant info.

    Returns:
        dict: Slack webhook payload.

    """

    restaurant_name = f'<{data.url}|{data.name}>' if data.url else data.name

    return {
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': f':knife_fork_plate: *{restaurant_name}*'
                }
            },
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': data.menu
                }
            }
        ]
    }


def post_menu(data: Restaurant) -> Response:
    """Posts a message to Slack

    Args:
        data (Restaurant): Restaurant info.

    Returns:
        requests.models.Response: Slack server response

    """
    payload = build_query_payload(data)

    return post_to_api(json=payload)


if __name__ == '__main__':
    test_data = Restaurant(name='Test 1', menu='Lots of food')
    res = post_menu(test_data)
    print('result', res)
