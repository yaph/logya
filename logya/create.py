import shutil
import sys
from importlib import resources

from logya.util import paths


def create(dir_site: str, name: str, site: str, **kwargs):
    target = paths(dir_site=dir_site).root.joinpath(name)
    if target.exists():
        sys.exit(f'Error: "{target}" already exists. Please remove it or specify another location.')

    source = resources.files(__name__).joinpath(f'sites/{site}')
    if source.is_dir():
        shutil.copytree(source, target)  # type: ignore
    else:
        sys.exit(f'The site "{site}" is not installed.')

    print(f'Site created in "{target}".')
