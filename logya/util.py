# -*- coding: utf-8 -*-
import re

from collections import namedtuple
from pathlib import Path
from string import punctuation, whitespace

from yaml import dump, load
try:
    from yaml import CDumper as Dumper, CLoader as Loader
except ImportError:
    from yaml import Dumper, Loader


# Characters not to be used in URLs, allowing some punctuation.
forbidden = (set(punctuation) - set('+-_.,@')) | set(whitespace)
re_forbidden = re.compile(f'[{re.escape("".join(forbidden))}]+')

directories = ['root', 'content', 'public', 'static', 'templates']
Paths = namedtuple('Paths', directories)


def deduplicate(li: list, attr: str) -> list:
    """Return a list without duplicates, based on value of given attribute."""
    result = []
    seen = set()
    for item in li:
        value = frozenset(item[attr])
        if value in seen:
            continue
        result.append(item)
        seen.add(value)
    return result


def encode_content(headers: dict, body: str) -> str:
    """Encode headers and body in content format."""

    return f'---\n{dump(headers, Dumper=Dumper).strip()}\n---\n{body}'


def load_yaml(text: str) -> dict:
    """Wrapper for yaml.load so yaml import is done only once."""

    return load(text, Loader=Loader)


def paths(dir_site: str = None) -> Paths:
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


def slugify(s: str) -> str:
    """Return string with forbidden characters replaced with hyphens.

    Consecutive forbidden characters are replaced with a single hyphen.
    Leading and trailing whitespace and hyphens are stripped.
    Different input strings may result in the same output.
    """
    return re.sub(re_forbidden, '-', s.strip()).strip('-')
