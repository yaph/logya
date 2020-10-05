# -*- coding: utf-8 -*-
import shutil

from shutil import copytree

from logya.core import Logya
from logya.content import write_collection, write_page


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

    print('Write documents.')
    for url, content in L.index.items():
        path_dst = L.paths.public.joinpath(url.lstrip('/'), 'index.html')
        if 'doc' in content:
            print(f'Write document page to: {path_dst}')
            write_page(path_dst, content, L.settings)
        elif 'docs' in content:
            print(f'Write collection page to: {path_dst}')
            write_collection(path_dst, content, L.settings)
