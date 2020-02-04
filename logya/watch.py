# -*- coding: utf-8 -*-
# TODOs
# Use watchgod to keep track of changes in `static` and `content` dirs.
# New and changed `static` files are copied to `public`.
# New files in `content` that have an allowed extension and not set to `noindex` result in a full rebuild of the index.
# In `do_GET` only update `content` and generated `index` pages.
import http.server
import socketserver

from functools import partial


HTTPRequestHandler = partial(http.server.SimpleHTTPRequestHandler, directory='deploy')


def serve(host='localhost', port=8080):
    with socketserver.TCPServer((host, port), HTTPRequestHandler) as httpd:
        print(f'Serving on http://{host}:{port}/')
        httpd.serve_forever()