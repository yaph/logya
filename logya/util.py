# -*- coding: utf-8 -*-
import re

import yaml

from pathlib import Path


# Characters not to be used in URLs
re_forbidden = re.compile(r'[^\.\w]+')


def load_settings():
    """Return a dictionary with global settings."""

    root = Path.cwd()
    settings = {
        'paths': {
            'root': root,
            'content': Path(root, 'content'),
            'templates': Path(root, 'templates'),
            'static': Path(root, 'static'),
            'public': Path(root, 'public')
        }
    }
    settings.update(yaml.load(Path(root, 'site.yaml').read_text(), Loader=yaml.FullLoader))
    return settings


def slugify(s: str) -> str:
    """Return string with forbidden characters replaced with hyphens.

    Consecutive forbidden characters are replaced with a single hyphen.
    Leading and trailing whitespace and hyphens are stripped.
    Different input strings may result in the same output.
    """
    return re.sub(re_forbidden, '-', s.strip()).strip('-')
