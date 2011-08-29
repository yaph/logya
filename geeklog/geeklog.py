#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import glob
import shutil
import ConfigParser

cwd = os.getcwd()
sys.path.append(os.path.join(cwd, 'lib'))
from docwriter import DocWriter
from jinja2 import Environment, PackageLoader

src_site = 'example_site' # TODO use command, e.g. ./geeklog run .
src = os.path.join(cwd, src_site)
config = ConfigParser.ConfigParser()
config.readfp(open(os.path.join(src, 'site.cfg')))
base_path = config.get('site', 'base_path')

template_env = Environment(loader=PackageLoader(src_site, 'templates'))
doc = DocWriter(base_path, template_env)

docs = glob.glob(os.path.join(src, 'posts', '*.html'))
doc.writedocs(docs)

# copy static files
src_static = os.path.join(src, 'static')
dst_static = os.path.join(cwd, 'site', 'static')
shutil.rmtree(dst_static, True)
shutil.copytree(src_static, dst_static)
