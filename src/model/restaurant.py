"""Data class for restaurant information"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Restaurant:
    """Restaurant information"""
    name: str
    menu: str
    url: str = None
