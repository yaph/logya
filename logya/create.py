# -*- coding: utf-8 -*-
import shutil
import sys

from importlib import resources

from logya.util import paths


def create(dir_site: str, name: str, site: str | None = None, **kwargs):
    target = paths(dir_site=dir_site).root.joinpath(name)
    if target.exists():
        sys.exit(f'Error: "{target}" already exists. Please remove it or specify another location.')
    try:
        source = resources.files(__name__).joinpath(f'sites/{site}')
    except KeyError:
        sys.exit(f'The site "{site}" is not installed.')
    else:
        shutil.copytree(source, target)
        print(f'Site created in "{target}".')
