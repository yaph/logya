#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from logya import __version__
from logya.create import Create
from logya.generate import generate
from logya.server import serve


def create(args):
    Create(args.name, site=args.site)


def main():
    parser = argparse.ArgumentParser(description='Logya a static Web site generator.')
    parser.add_argument('--version', '-V', action='version', version=__version__)
    parser.add_argument('--verbose', '-v', action='store_true', help='Print log messages during execution.')

    subparsers = parser.add_subparsers()

    # create a basic site with the given name
    p_create = subparsers.add_parser('create', help='Create a starter Web site in the specified directory.')
    p_create.add_argument('name', help='name of the directory to create.')
    p_create.set_defaults(func=create)
    p_create.add_argument('--site', '-s', default='starter', help='Name one of the available sites.')

    # generate a site in public directory, generate and gen sub commands do the same
    hlp = 'Generate Web site to public from current directory.'
    hlp_dir_site = ('Path to Web site directory, absolute or relative to current working directory.')
    hlp_keep = ('Keep existing `public` directory, by default it is removed.')
    for command in ['generate', 'gen']:
        p_gen = subparsers.add_parser(command, help=hlp)
        p_gen.set_defaults(func=generate)
        p_gen.add_argument('--dir_site', '-d', help=hlp_dir_site)
        p_gen.add_argument('--keep', '-k', action='store_true', default=False, help=hlp_keep)

    # serve static pages
    p_serve = subparsers.add_parser('serve', help='Serve static pages from public directory.')
    p_serve.set_defaults(func=serve)
    p_serve.add_argument('--host', '-a', default='localhost', help='server host name or IP')
    p_serve.add_argument('--port', '-p', default=8080, type=int, help='server port to listen')

    args = parser.parse_args()
    if getattr(args, 'func', None):
        args.func(args)


if __name__ == '__main__':
    main()
