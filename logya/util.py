# -*- coding: utf-8 -*-
import re

import yaml

from collections import namedtuple
from pathlib import Path

# FIXME document breaking change from dir_*
# FIXME make root, content and templates required
cwd = Path.cwd()
Paths = namedtuple('Paths', ['root', 'content', 'templates', 'static', 'public'])
paths = Paths(
    root=cwd,
    content=Path(cwd, 'content'),
    templates=Path(cwd, 'templates'),
    static=Path(cwd, 'static'),
    public=Path(cwd, 'public')
)

# Load site config
config = yaml.load(Path(paths.root, 'site.yaml').read_text(), Loader=yaml.FullLoader)

# Characters not to used in URLs
re_forbidden = re.compile(r'[^\.\w]+')


def slugify(s: str) -> str:
    """Return string with forbidden characters replaced with hyphens.

    Consecutive forbidden characters are replaced with a single hyphen.
    Leading and trailing whitespace and hyphens are stripped.
    Different input strings may result in the same output.
    """
    return re.sub(re_forbidden, '-', s.strip()).strip('-')


