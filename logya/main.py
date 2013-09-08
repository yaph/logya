#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from logya import __version__
from logya.create import Create
from logya.generate import Generate
from logya.serve import Serve
from logya.test import Test


def create(args):
    Create(args.name)


def generate(args):
    Generate(verbose=args.verbose)


def serve(args):
    Serve(host=args.host, port=args.port)


def test(args):
    Test()


def main():
    parser = argparse.ArgumentParser(
        description='Logya a static Web site generator.')
    parser.add_argument(
        '--version', action='version', version=__version__)
    parser.add_argument(
        '--verbose', action="store_true", default=False, help='print messages')

    subparsers = parser.add_subparsers()

    # create a basic site with the given name
    p_create = subparsers.add_parser(
        'create', help='create starter Web site in the specified directory')
    p_create.add_argument('name', help='name of the directory to create.')
    p_create.set_defaults(func=create)

    # generate a site for deployment, generate and gen sub commands do the same
    msg = 'generate Web site to deploy from current directory'
    [subparsers.add_parser(
        c, help=msg).set_defaults(func=generate) for c in ['generate', 'gen']]

    # serve static pages
    sp_serve = subparsers.add_parser(
        'serve', help='serve static pages from deploy directory')
    sp_serve.set_defaults(func=serve)
    sp_serve.add_argument('--port', type=int, help='server port to listen')
    sp_serve.add_argument('--host', help='server host name or IP')

    # test stuff
    subparsers.add_parser('test', help='test stuff').set_defaults(func=test)

    # process arguments
    args = parser.parse_args()
    if getattr(args, 'func', None):
        args.func(args)

if __name__ == "__main__":
    main()