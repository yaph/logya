#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import glob
import shutil

cwd = os.getcwd()
sys.path.append(os.path.join(cwd, 'lib'))

from docwriter import DocWriter
from jinja2 import Environment, PackageLoader

template_env = Environment(loader=PackageLoader('example_site', 'templates'))
doc = DocWriter(template_env)

docs = glob.glob(os.path.join(cwd, 'example_site', 'posts', '*.html'))
doc.writedocs(docs)

# copy static files
src = os.path.join(cwd, 'example_site', 'static')
dst = os.path.join(cwd, 'site', 'static')
shutil.rmtree(dst, True)
shutil.copytree(src, dst)
