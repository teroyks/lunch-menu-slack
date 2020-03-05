"""Miscellaneous helpers"""
from dataclasses import dataclass


@dataclass(frozen=True)
class MenuMsg:
    """Menu text in case of an error."""
    URL_NOT_FOUND = 'Lunch menu page not found'
    MENU_NOT_FOUND = 'Not found'
