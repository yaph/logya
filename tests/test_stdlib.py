#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import ChainMap


d1 = {
    '/': {'name': 'd1 /'},
    '/a/': {'name': 'd1 /a/'},
    '/b/': {'name': 'd1 /b/'},
}

d2 = {
    '/': {'name': 'd2 /'},
    '/b/': {'name': 'd2 /b/'},
    '/c/': {'name': 'd2 /c/'},
}

cm = ChainMap(d1, d2)