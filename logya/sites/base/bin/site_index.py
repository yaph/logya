# -*- coding: utf-8 -*-
# Run this script from your Logya site directory, e. g.:
# python bin/site_index.py
import json

from logya.core import Logya
from logya.encoder import JSONEncoder


L = Logya()
L.build()
site_index = {}

for url, doc in L.index.items():
    del doc['body']
    site_index[url] = doc

index_file = L.paths.static.joinpath('site_index.json')
index_file.write_text(json.dumps(site_index, cls=JSONEncoder))