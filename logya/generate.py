import shutil
from shutil import copytree

from logya.content import write_collection, write_page
from logya.core import Logya


def generate(dir_site: str, verbose: bool, keep: bool, **kwargs):
    L = Logya(dir_site=dir_site, verbose=verbose)
    L.build()

    if not keep:
        print('Remove existing public directory.')
        shutil.rmtree(L.paths.public, ignore_errors=True)

    print(f'Generate site in directory: {L.paths.public.as_posix()}')
    if L.paths.static.exists():
        print('Copy static files.')
        copytree(L.paths.static, L.paths.public, dirs_exist_ok=True)  # dirs_exist_ok requires Python 3.8

    print('Write pages.')
    for url, content in L.doc_index.items():
        L.info(f'Write content: {url}')
        write_page(L.paths.public, content['doc'])

    for url, content in L.collection_index.items():
        L.info(f'Write collection: {url}')
        write_collection(L.paths.public, content)
