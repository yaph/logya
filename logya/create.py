# -*- coding: utf-8 -*-
import shutil

from pkg_resources import resource_filename

from logya.util import paths


def create(options):
    target = paths(dir_site=options.dir_site).root.joinpath(options.name)
    if target.exists():
        print(f'Error: "{target}" already exists. Please remove it or specify another location.')
        return
    try:
        source = resource_filename(__name__, 'sites/' + options.site)
    except KeyError:
        print(f'The site "{options.site}" is not installed.')
    else:
        print(f'Site created in "{target}".')
        shutil.copytree(source, target)
