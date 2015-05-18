# -*- coding: utf-8 -*-
# Run this script from your Logya site directory, e. g.:
# python scripts/site_index.py
import io
import os
import json

from logya.core import Logya
from logya.encoder import JSONEncoder


logya = Logya()
logya.init_env()
logya.build_index()

site_index = {}
for url, doc in logya.docs.items():
    del doc['body']
    site_index[url] = doc

index_file = os.path.join(logya.dir_static, 'site_index.json')
with io.open(index_file, 'w', encoding='utf-8') as f:
    json.dump(site_index, f, cls=JSONEncoder)
