# -*- coding: utf-8 -*-
import json
import os

from datetime import datetime


def date_handler(obj):
    return obj.isoformat() if isinstance(obj, datetime) else obj


logya = globals()['logya']
logya.build_indexes()

site_index = {}
for url, doc in logya.docs_parsed.items():
    del doc['body']
    site_index[url] = doc

with open(os.path.join(logya.dir_static, 'site_index.json'), 'w') as f:
    json.dump(site_index, f, default=date_handler)
