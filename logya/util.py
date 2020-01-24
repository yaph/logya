# -*- coding: utf-8 -*-
import re

# Characters not to used in URLs
re_forbidden = re.compile(r'[^\.\w]+')


def slugify(s: str) -> str:
    """Return string with forbidden characters replaced with hyphens.

    Consecutive forbidden characters are replaced with a single hyphen.
    Leading and trailing whitespace and hyphens are stripped.
    Different input strings may result in the same output.
    """
    return re.sub(re_forbidden, '-', s.strip()).strip('-')