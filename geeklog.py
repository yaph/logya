#!/usr/bin/python
import os
import glob
import sys

cwd = os.getcwd()

sys.path.append(os.path.join(cwd, 'lib'))
from docwriter import DocWriter

posts = glob.glob(os.path.join(cwd, 'posts', '*.html'))
for p in posts:
    doc = DocWriter(p)
    doc.write()
