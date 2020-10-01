# -*- coding: utf-8 -*-
import shutil

from pathlib import Path
from shutil import copytree

from logya.core import Logya
from logya.content import read_all, write_collection, write_page
from logya.util import load_settings


def generate(args):
    L = Logya()
    L.init_env()
    settings = load_settings()
    path_public = settings['paths']['public']
    path_static = settings['paths']['static']

    if not args.keep:
        print('Remove existing public directory.')
        shutil.rmtree(path_public, ignore_errors=True)

    print(f'Generate site in directory: {path_public.as_posix()}')
    if path_static.exists():
        print('Copy static files.')
        copytree(path_static, path_public, dirs_exist_ok=True)  # dirs_exist_ok requires Python 3.8

    site_index = read_all(settings)
    print('Write documents.')
    for url, content in site_index.items():
        path_dst = Path(path_public, url.lstrip('/'), 'index.html')
        if 'doc' in content:
            print(f'Write document page to: {path_dst}')
            write_page(path_dst, content, L.template, settings)
        elif 'docs' in content:
            print(f'Write collection page to: {path_dst}')
            write_collection(path_dst, content, L.template, settings)
