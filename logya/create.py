# -*- coding: utf-8 -*-
import shutil

from sys import exit

from pkg_resources import resource_filename

from logya.util import paths


def create(dir_site: str, name: str, site: str = None, **kwargs):
    target = paths(dir_site=dir_site).root.joinpath(name)
    if target.exists():
        exit(f'Error: "{target}" already exists. Please remove it or specify another location.')
    try:
        source = resource_filename(__name__, f'sites/{site}')
    except KeyError:
        exit(f'The site "{site}" is not installed.')
    else:
        shutil.copytree(source, target)
        print(f'Site created in "{target}".')
