# -*- coding: utf-8 -*-
import shutil

from shutil import copytree

from logya.core import Logya
from logya.content import filepath, write_collection, write_page


def generate(options):
    L = Logya(options)
    L.build()

    if not options.keep:
        print('Remove existing public directory.')
        shutil.rmtree(L.paths.public, ignore_errors=True)

    print(f'Generate site in directory: {L.paths.public.as_posix()}')
    if L.paths.static.exists():
        print('Copy static files.')
        copytree(L.paths.static, L.paths.public, dirs_exist_ok=True)  # dirs_exist_ok requires Python 3.8

    print('Write pages.')
    for url, content in L.index.items():
        path_dst = filepath(L.paths.public, url)
        L.info(f'Write content: {path_dst}')
        write_page(path_dst, content, L.settings)

    for name, coll in L.collections.items():
        for url, content in coll['index'].items():
            path_dst = filepath(L.paths.public, url)
            L.info(f'Write collection: {path_dst}')
            write_collection(path_dst, content, L.settings)
