#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from logya import __version__
from logya.create import Create
from logya.generate import Generate
from logya.serve import Serve


def create(args):
    Create(args.name, site=args.site)


def generate(args):
    Generate(verbose=args.verbose, dir_site=args.dir_site, keep=args.keep)


def serve(args):
    Serve(host=args.host, port=args.port)


def main():
    parser = argparse.ArgumentParser(
        description='Logya a static Web site generator.')
    parser.add_argument(
        '--version', action='version', version=__version__)
    parser.add_argument(
        '--verbose', action='store_true', default=False, help='print messages')

    subparsers = parser.add_subparsers()

    # create a basic site with the given name
    p_create = subparsers.add_parser(
        'create', help='Create a starter Web site in the specified directory.')
    p_create.add_argument('name', help='name of the directory to create.')
    p_create.set_defaults(func=create)
    p_create.add_argument('--site', default='starter', help='Name one of the available sites.')

    # generate a site for deployment, generate and gen sub commands do the same
    hlp = 'Generate Web site to deploy from current directory.'
    hlp_dir_site = ('Path to Web site directory, absolute or relative to '
                    'current working directory.')
    hlp_keep = ('Keep existing deply directory, by default it is removed.')
    for command in ['generate', 'gen']:
        p_gen = subparsers.add_parser(command, help=hlp)
        p_gen.set_defaults(func=generate)
        p_gen.add_argument('--dir_site', help=hlp_dir_site)
        p_gen.add_argument('--keep', action='store_true', default=False, help=hlp_keep)

    # serve static pages
    p_serve = subparsers.add_parser(
        'serve', help='Serve static pages from deploy directory.')
    p_serve.set_defaults(func=serve)
    p_serve.add_argument('--port', type=int, help='server port to listen')
    p_serve.add_argument('--host', help='server host name or IP')

    args = parser.parse_args()
    if getattr(args, 'func', None):
        args.func(args)


if __name__ == '__main__':
    main()
