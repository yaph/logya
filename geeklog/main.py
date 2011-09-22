#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __init__ import __version__
import argparse
from geeklog import Geeklog

def create(args):
    Geeklog().create(args.name)

def generate(args):
    Geeklog().generate()

def help(args):
    args.parser.print_help()

def main():
    parser = argparse.ArgumentParser(description='Geeklog a static Web site generator.', version=__version__)
    subparsers = parser.add_subparsers()

    # create a basic site with the given name
    p_create = subparsers.add_parser('create', help='Create the basis for a Web site in the directory with the specified name.')
    p_create.add_argument('name', help='The name of the Web site to create.')
    p_create.set_defaults(func=create)

    # generate a site for deployment, generate and gen sub commands do the same
    msg_generate = 'Generate the Web site to deploy from the current directory.'
    p_generate = subparsers.add_parser('generate', help=msg_generate)
    p_generate.set_defaults(func=generate)
    p_gen = subparsers.add_parser('gen', help=msg_generate)
    p_generate.set_defaults(func=generate)

    # make help act the same as -h and --help
    p_help = subparsers.add_parser('help')
    p_help.set_defaults(func=help, parser=parser)

    # process arguments
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
