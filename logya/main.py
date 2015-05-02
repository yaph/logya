#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from logya import __version__
from logya.create import Create
from logya.generate import Generate
from logya.serve import Serve
from logya.run import Run


def create(args):
    Create(args.name)


def generate(args):
    Generate(verbose=args.verbose)


def serve(args):
    Serve(host=args.host, port=args.port)


def run(args):
    Run(args.script)


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
        'create', help='Create a starter Web site in the specified directory.')
    p_create.add_argument('name', help='name of the directory to create.')
    p_create.set_defaults(func=create)

    # generate a site for deployment, generate and gen sub commands do the same
    msg = 'Generate Web site to deploy from current directory.'
    for command in ['generate', 'gen']:
        subparsers.add_parser(command, help=msg).set_defaults(func=generate)

    # serve static pages
    p_serve = subparsers.add_parser(
        'serve', help='Serve static pages from deploy directory.')
    p_serve.set_defaults(func=serve)
    p_serve.add_argument('--port', type=int, help='server port to listen')
    p_serve.add_argument('--host', help='server host name or IP')

    # run script in Logya context
    p_run = subparsers.add_parser('run', help='Run script in Logya context.')
    p_run.add_argument('script', help='Python script to execute.')
    p_run.set_defaults(func=run)

    # process arguments
    args = parser.parse_args()
    if getattr(args, 'func', None):
        args.func(args)

if __name__ == '__main__':
    main()
