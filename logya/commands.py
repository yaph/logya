import shutil
import sys
from importlib import resources
from os import walk
from pathlib import Path

from logya.content import write_collection, write_page
from logya.core import Logya
from logya.util import latest_file_change, paths


def clean(dir_site: str, verbose: bool, **_kwargs) -> None:
    """Remove files not found in the site's index and empty directories from public directory."""

    L = Logya(dir_site=dir_site, verbose=verbose)
    L.build()

    search_index = L.collection_index.copy()
    search_index.update(L.doc_index)

    # Walk bottom up so empty directories can be removed in the same loop as stale files.
    for r, dirs, files in walk(L.paths.public, topdown=False):
        root = Path(r)
        # Remove stale files
        for f in files:
            rel_file = root.relative_to(L.paths.public).joinpath(f)
            url = '/' + rel_file.as_posix()
            if url in search_index:
                continue
            if url.endswith('index.html') and url.rstrip('index.html') in search_index:
                continue
            if L.paths.static.joinpath(rel_file).exists():
                continue

            stale_file = Path(root, f)
            L.info(f'Remove stale file: {stale_file}')
            stale_file.unlink()

        # Remove empty directories unless they exist in the site's `static` directory.
        for d in dirs:
            # Check static directory first to avoid unnecessary work.
            rel_dir = root.relative_to(L.paths.public).joinpath(d)
            if L.paths.static.joinpath(rel_dir).exists():
                continue
            # Keep populated directories.
            check_dir = Path(root, d)
            if any(check_dir.iterdir()):
                continue

            L.info(f'Remove empty directory: {check_dir}')
            check_dir.rmdir()


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


def generate(dir_site: str, verbose: bool, **_kwargs):
    """Generate a site in the public directory."""

    L = Logya(dir_site=dir_site, verbose=verbose)
    L.build()

    mtime_templates = latest_file_change(L.paths.templates.as_posix())

    print(f'Generate site in directory: {L.paths.public.as_posix()}')
    if L.paths.static.exists():
        print('Copy static files.')
        shutil.copytree(L.paths.static, L.paths.public, dirs_exist_ok=True)

    print('Write pages.')
    for url, content in L.doc_index.items():
        L.info(f'Write content: {url}')
        write_page(L.paths.public, content['doc'], min_mtime=max(mtime_templates, content['path'].stat().st_mtime))

    for url, content in L.collection_index.items():
        L.info(f'Write collection: {url}')
        write_collection(L.paths.public, content)
