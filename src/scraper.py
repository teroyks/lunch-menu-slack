"""Fetches menus for all the restaurants found in the restaurants package"""

from importlib import import_module
from multiprocessing import Pool
from typing import Generator, Optional

from model.restaurant import Restaurant
from restaurants import __all__ as restaurant_modules


def _fetch_menu(module_name: str) -> Optional[Restaurant]:
    try:
        mod = import_module(f'.{module_name}', 'restaurants')
        return mod.fetch()  # type: ignore
    except (AttributeError, ModuleNotFoundError) as e:
        print(e)
        return None


def fetch_menus() -> Generator[Restaurant, None, None]:
    """Fetches menus for all the restaurants.

    Yields:
        Restaurant: The next fetched restaurant info, in order the results are received

    """
    with Pool(processes=10) as pool:
        results = pool.imap_unordered(_fetch_menu, restaurant_modules)
        yield from (r for r in results if r)


if __name__ == '__main__':
    for m in fetch_menus():
        print(m)
