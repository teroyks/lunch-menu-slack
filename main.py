"""Fetches the lunch menus for all the restaurants and posts to Slack."""

import argparse

from slack import post_menu
from scraper import fetch_menus

parser = argparse.ArgumentParser(description='Post restaurant menus to Slack.')
parser.add_argument('-p', '--print', dest='print_only', action='store_true',
                    help='print restaurant info, do not post to Slack')
args = parser.parse_args()

for menu in fetch_menus():
    if args.print_only:
        print(menu)
    else:
        post_menu(menu)
