# -*- coding: utf-8 -*-
import io
import os
import json

from logya.encoder import JSONEncoder


logya = globals()['logya']
logya.build_indexes()

site_index = {}
for url, doc in logya.docs_parsed.items():
    del doc['body']
    site_index[url] = doc

index_file = os.path.join(logya.dir_static, 'site_index.json')
with io.open(index_file, 'w', encoding='utf-8') as f:
    json.dump(site_index, f, cls=JSONEncoder)
