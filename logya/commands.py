import shutil
import sys
from importlib import resources
from pathlib import Path

from logya.content import write_collection, write_page
from logya.core import Logya
from logya.util import paths


def clean(dir_site: str, **kwargs) -> None:
    L = Logya(dir_site=dir_site, verbose=kwargs.get('verbose'))
    L.build()

    search_index = L.collection_index.copy()
    search_index.update(L.doc_index)

    for root, _, files in L.paths.public.walk():
        for f in files:
            rel_file = root.relative_to(L.paths.public).joinpath(f)
            url = '/' + rel_file.as_posix()

            if url in search_index or url.replace('index.html', '') in search_index:
                continue
            if L.paths.static.joinpath(rel_file).exists():
                continue

            stale_file = Path(root, f)
            L.info(f'Remove: {stale_file} - {url}')
            stale_file.unlink()


def create(dir_site: str, name: str, site: str, **_kwargs) -> None:
    """Create a new site in the specified directory."""

    target = paths(dir_site=dir_site).root.joinpath(name)
    if target.exists():
        sys.exit(f'Error: "{target}" already exists. Please remove it or specify another location.')

    source = resources.files('logya').joinpath(f'sites/{site}')
    if source.is_dir():
        shutil.copytree(source, target)  # type: ignore
    else:
        sys.exit(f'The site "{site}" is not installed.')

    print(f'Site created in "{target}".')


def generate(dir_site: str, keep: bool, **kwargs):
    """Generate a site in the public directory."""

    L = Logya(dir_site=dir_site, verbose=kwargs.get('verbose'))
    L.build()

    mtime_templates = None
    if keep:
        mtime_templates = L.paths.templates.stat().st_mtime
    else:
        print('Remove existing public directory.')
        shutil.rmtree(L.paths.public, ignore_errors=True)

    print(f'Generate site in directory: {L.paths.public.as_posix()}')
    if L.paths.static.exists():
        print('Copy static files.')
        shutil.copytree(L.paths.static, L.paths.public, dirs_exist_ok=True)

    print('Write pages.')
    for url, content in L.doc_index.items():
        L.info(f'Write content: {url}')
        min_mtime = max(mtime_templates, content['path'].stat().st_mtime) if keep else None
        write_page(L.paths.public, content['doc'], min_mtime=min_mtime)

    for url, content in L.collection_index.items():
        L.info(f'Write collection: {url}')
        write_collection(L.paths.public, content)
