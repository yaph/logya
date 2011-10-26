#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __init__ import __version__
import argparse
from logya import Logya

def create(args):
    Logya().create(args.name)

def generate(args):
    Logya().generate()

def serve(args):
    Logya().serve()

def test(args):
    Logya().test()

def main():
    parser = argparse.ArgumentParser(description='Logya a static Web site generator.', version=__version__)
    subparsers = parser.add_subparsers()

    # create a basic site with the given name
    p_create = subparsers.add_parser('create', help='Create the basis for a Web site in the directory with the specified name.')
    p_create.add_argument('name', help='The name of the Web site to create.')
    p_create.set_defaults(func=create)

    # generate a site for deployment, generate and gen sub commands do the same
    msg = 'Generate the Web site to deploy from the current directory.'
    [subparsers.add_parser(c, help=msg).set_defaults(func=generate) for c in ['generate', 'gen']]

    # serve static pages
    subparsers.add_parser('serve', help='Serve static pages from deploy directory.').set_defaults(func=serve)

    # test stuff
    subparsers.add_parser('test', help='Test stuff.').set_defaults(func=test)

    # process arguments
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()