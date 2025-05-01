import shutil
import sys
from importlib import resources

from logya.content import write_collection, write_page
from logya.core import Logya
from logya.util import paths


def create(dir_site: str, name: str, site: str, **_kwargs) -> None:
    """Create a new site in the specified directory."""

    target = paths(dir_site=dir_site).root.joinpath(name)
    if target.exists():
        sys.exit(f'Error: "{target}" already exists. Please remove it or specify another location.')

    source = resources.files(__name__).joinpath(f'sites/{site}')
    if source.is_dir():
        shutil.copytree(source, target)  # type: ignore
    else:
        sys.exit(f'The site "{site}" is not installed.')

    print(f'Site created in "{target}".')


def generate(dir_site: str, verbose: bool, keep: bool, **_kwargs):
    """Generate a site in the public directory."""

    L = Logya(dir_site=dir_site, verbose=verbose)
    L.build()

    if not keep:
        print('Remove existing public directory.')
        shutil.rmtree(L.paths.public, ignore_errors=True)

    print(f'Generate site in directory: {L.paths.public.as_posix()}')
    if L.paths.static.exists():
        print('Copy static files.')
        shutil.copytree(L.paths.static, L.paths.public, dirs_exist_ok=True)

    print('Write pages.')
    for url, content in L.doc_index.items():
        L.info(f'Write content: {url}')
        write_page(L.paths.public, content['doc'])

    for url, content in L.collection_index.items():
        L.info(f'Write collection: {url}')
        write_collection(L.paths.public, content)
