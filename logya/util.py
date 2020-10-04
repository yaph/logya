# -*- coding: utf-8 -*-
import re

from collections import namedtuple
from pathlib import Path

from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


# Characters not to be used in URLs
re_forbidden = re.compile(r'[\s\/\?\+\{\}\|\\\[\]:;&$=]+')

directories = ['root', 'content', 'public', 'static', 'templates']
Paths = namedtuple('Paths', directories)


# FIXME use tests in test_canonical_filename
def filepath(base: Path, url: str) -> Path:
    """Get a Path object pointing to a file.

    If url does not end in a file name 'index.html' will be appended.
    """

    path = Path(base, url.lstrip('/'))
    if not path.suffix:
        path = path.joinpath('index.html')
    return path


def paths(dir_site: str = None) -> dict:
    if dir_site:
        root = Path(dir_site)
    else:
        root = Path.cwd()

    return Paths(
        root=root,
        content=root.joinpath('content'),
        templates=root.joinpath('templates'),
        static=root.joinpath('static'),
        public=root.joinpath('public')
    )


def load_yaml(text: str) -> dict:
    return load(text, Loader=Loader)


# FIXME use tests in test_slugify
def slugify(s: str) -> str:
    """Return string with forbidden characters replaced with hyphens.

    Consecutive forbidden characters are replaced with a single hyphen.
    Leading and trailing whitespace and hyphens are stripped.
    Different input strings may result in the same output.
    """
    return re.sub(re_forbidden, '-', s.strip()).strip('-')
