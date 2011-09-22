#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __init__ import __version__
import argparse
from geeklog import Geeklog

def create(args):
    Geeklog().create(args.name)

def generate(args):
    Geeklog().generate()

def main():
    parser = argparse.ArgumentParser(description='Geeklog a static Web site generator.', version=__version__)
    subparsers = parser.add_subparsers()

    p_create = subparsers.add_parser('create', help='Create the basis for a Web site in the directory with the specified name.')
    p_create.add_argument('name', help='The name of the Web site to create.')
    p_create.set_defaults(func=create)

    p_generate = subparsers.add_parser('generate', help='Generate the Web site to deploy from the current directory.')
    p_generate.set_defaults(func=generate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
