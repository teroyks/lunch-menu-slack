"""Include all modules in the directory"""

from os import path, scandir, DirEntry


def _is_restaurant_module(entry: DirEntry) -> bool:
    """Checks if entry is a Python file, ignores if name starts with underscore."""
    return all([
        entry.is_file(),
        entry.name.endswith('.py'),  # type: ignore
        not entry.name.startswith('_')  # type: ignore
    ])


def _module_name(filename: str) -> str:
    return path.splitext(filename)[0]


with scandir(path.dirname(__file__)) as dir_it:
    __all__ = [_module_name(entry.name)
               for entry in dir_it if _is_restaurant_module(entry)]
