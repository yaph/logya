import re
from pathlib import Path
from string import punctuation, whitespace
from typing import NamedTuple

from yaml import dump, load

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
    content: Path
    public: Path
    static: Path
    templates: Path


def cache(func):
    """Decorator for caching function calls."""

    mapping = {}

    def f(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mapping:
            mapping[key] = func(*args, **kwargs)
        return mapping[key]
    return f


def encode_content(headers: dict, body: str) -> str:
    """Encode headers and body in content format."""

    return f'---\n{dump(headers, Dumper=Dumper).strip()}\n---\n{body}'


def load_yaml(text: str) -> dict:
    """Wrapper for yaml.load so yaml import is done only once."""

    return load(text, Loader=Loader)  # noqa: S506


def paths(dir_site: str) -> Paths:
    root = Path(dir_site)
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
