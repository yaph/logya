import os
import re
import sys
from functools import lru_cache
from pathlib import Path
from string import punctuation, whitespace
from typing import NamedTuple

from yaml import YAMLError, dump, load

try:
    from yaml import CDumper as Dumper
    from yaml import CLoader as Loader
except ImportError:  # pragma: no cover
    from yaml import Dumper, Loader  # type: ignore


# Characters not to be used in URLs, allowing some punctuation.
forbidden = (set(punctuation) - set('+-_.,@')) | set(whitespace)
re_forbidden = re.compile(f'[{re.escape("".join(forbidden))}]+')


# For accessing site paths.
class Paths(NamedTuple):
    root: Path
    cache: Path
    content: Path
    public: Path
    static: Path
    templates: Path


def encode_content(headers: dict, body: str) -> str:
    """Encode headers and body in content format."""

    return f'---\n{dump(headers, Dumper=Dumper).strip()}\n---\n{body.strip()}'


def load_yaml(text: str) -> dict:
    """Wrapper for yaml.load so yaml import is done only once."""

    try:
        return load(text, Loader=Loader)  # noqa: S506
    except YAMLError as err:
        sys.exit(f'Error loading YAML:\n{text}\n{err}\nExiting...')


def paths(dir_site: str) -> Paths:
    root = Path(dir_site)
    return Paths(
        root=root,
        cache=root.joinpath('.cache'),
        content=root.joinpath('content'),
        templates=root.joinpath('templates'),
        static=root.joinpath('static'),
        public=root.joinpath('public'),
    )


@lru_cache(maxsize=256)
def slugify(s: str) -> str:
    """Return string with forbidden characters replaced with hyphens. Different input strings may result in the same output.

    Consecutive forbidden characters are replaced with a single hyphen. Leading and trailing whitespace is stripped.
    """
    return re.sub(re_forbidden, '#', s.strip()).strip('#').replace('#', '-')


def latest_file_change(root: str):
    """Return mtime of the most recently edited file in root."""

    latest_mtime = 0.0

    def walk_dir(path):
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_dir(follow_symlinks=False):
                    yield from walk_dir(entry.path)
                else:
                    yield entry

    for entry in walk_dir(root):
        try:
            mtime = entry.stat().st_mtime
        except FileNotFoundError:  # skip race condition
            continue
        if mtime > latest_mtime:
            latest_mtime = mtime

    return latest_mtime
