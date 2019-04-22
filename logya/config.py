# -*- coding: utf-8 -*-
# Site configuration access.

import io
import yaml


def load(filename):
    """Create config object read from the given file."""

    with io.open(filename, 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)
