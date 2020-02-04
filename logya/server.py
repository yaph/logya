# -*- coding: utf-8 -*-
# TODOs
# Use watchgod to keep track of changes in `static` and `content` dirs.
# New and changed `static` files are copied to `public`.
# New files in `content` that have an allowed extension and not set to `noindex` result in a full rebuild of the index.
# In `do_GET` only update `content` and generated `index` pages.
import http.server
import socketserver

from pathlib import Path
from shutil import copyfile
from urllib.parse import unquote, urlparse

from logya.util import paths


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler based class to return resources."""

    def __init__(self, *args):
        super(HTTPRequestHandler, self).__init__(*args, directory=paths.public.as_posix())

    def do_GET(self):
        """Return refreshed resource."""

        update_resource(self.path)
        super(HTTPRequestHandler, self).do_GET()


def update_resource(url_path):
    # Use only the actual path and ignore possible query params issue #3.
    src_url = unquote(urlparse(url_path).path)
    src_name = src_url.lstrip('/')

    # If a static file is requested update it and return.
    src_static = Path(paths.static, src_name)
    if src_static.is_file():
        dst_static = Path(paths.public, src_name)
        dst_static.parent.mkdir(exist_ok=True)
        if not dst_static.exists() or src_static.stat().st_mtime > dst_static.stat().st_mtime:
            print(f'Update static resource: {dst_static}')
            copyfile(src_static, dst_static)
        return True


def serve(args):
    with socketserver.TCPServer((args.host, args.port), HTTPRequestHandler) as httpd:
        print(f'Serving on http://{args.host}:{args.port}/')
        httpd.serve_forever()