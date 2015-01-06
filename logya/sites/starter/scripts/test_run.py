# -*- coding: utf-8 -*-

logya = globals()['logya']
logya.build_indexes()
print([d['title'] for u, d in logya.docs_parsed.items()])
