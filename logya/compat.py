# -*- coding: utf-8 -*-

"""
logya.compat
~~~~~~~~~~~~~

Imports and declarations for Python 2 and Python 3 compatibility.
Based on
https://github.com/michaelhelmick/lassie/blob/master/lassie/compat.py
"""

import sys

is3 = sys.version_info[0] == 3

if is3:
    from urllib.parse import quote_plus
    from urllib.parse import urlparse
    from http.server import SimpleHTTPRequestHandler
    from http.server import HTTPServer

else:
    from urllib import quote_plus
    from urlparse import urlparse
    from SimpleHTTPServer import SimpleHTTPRequestHandler
    from BaseHTTPServer import HTTPServer
