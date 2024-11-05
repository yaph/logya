#!/usr/bin/env python
import argparse

from logya import __version__
from logya.create import create
from logya.generate import generate
from logya.server import serve


def main():
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument('--verbose', '-v', action='store_true', help='Print info messages during execution.')
    parent.add_argument('--dir-site', '-d', default='.', help='Path to site directory, absolute or relative to current working directory.')

    parser = argparse.ArgumentParser(description='Logya a static site generator.')
    parser.add_argument('--version', '-V', action='version', version=__version__)
    subparsers = parser.add_subparsers()

    # create a basic site with the given name
    p_create = subparsers.add_parser('create', parents=[parent], help='Create a starter site in the specified directory.')
    p_create.add_argument('name', help='name of the directory to create.')
    p_create.set_defaults(func=create)
    p_create.add_argument('--site', '-s', default='base', help='Name one of the available sites.')

    # generate a site in public directory, generate and gen sub commands do the same
    p_generate = subparsers.add_parser('generate', aliases=('gen',), parents=[parent], help='Generate site in public directory.')
    p_generate.set_defaults(func=generate)
    hlp_keep = 'Keep existing `public` directory, by default it is removed.'
    p_generate.add_argument('--keep', '-k', action='store_true', default=False, help=hlp_keep)

    # serve static pages
    p_serve = subparsers.add_parser('serve', parents=[parent], help='Serve static pages from public directory.')
    p_serve.set_defaults(func=serve)
    p_serve.add_argument('--host', '-a', default='localhost', help='server host name or IP')
    p_serve.add_argument('--port', '-p', default=8080, type=int, help='server port to listen')

    args = parser.parse_args()
    if getattr(args, 'func', None):
        args.func(**vars(args))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
