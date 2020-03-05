"""Data class for restaurant information"""
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Restaurant:
    """Restaurant information"""
    name: str
    menu: str
    url: Optional[str] = None
