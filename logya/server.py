# -*- coding: utf-8 -*-
import http.server
import socketserver

from shutil import copyfile
from urllib.parse import unquote, urlparse

from logya.core import Logya
from logya.content import read, write_collection, write_page
from logya.template import env
from logya.util import filepath


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler based class to return resources."""

    L = None

    def __init__(self, *args):
        super(HTTPRequestHandler, self).__init__(*args, directory=self.L.paths.public.as_posix())

    def do_GET(self):
        update_resource(self.path, self.L)
        super(HTTPRequestHandler, self).do_GET()


def update_resource(path, L):
    """Update resource corresponding to given url.

    Resources that exist in the `static` directory are updated if they are newer than the destination file.
    For other HTML resources the whole `L.index` is updated and the destination is newly written."""

    # Use only the actual path and ignore possible query params (see issue #3).
    url = unquote(urlparse(path).path)
    url_rel = path.lstrip('/')
    path_dst = filepath(L.paths.public, url)

    # If a static file is requested update it and return.
    src_static = L.paths.static.joinpath(url_rel)
    if src_static.is_file():
        dst_static = L.paths.public.joinpath(url_rel)
        dst_static.parent.mkdir(exist_ok=True)
        if not dst_static.exists() or src_static.stat().st_mtime > dst_static.stat().st_mtime:
            L.info(f'Update static resource: {dst_static}')
            copyfile(src_static, dst_static)
        return

    # Update content page.
    if content := L.index.get(url):
        content['doc'] = read(content['path'], content['path'].relative_to(L.paths.content))
        if L.collections:
            L.update_collections(content['doc'])
        # Always write doc because of possible template changes.
        write_page(path_dst, content, L.settings)
        L.info(f'Refreshed doc at URL: {path}')

    # Update collection page.
    elif coll := L.collections.get(url.split('/')[1]):
        if content := coll['index'].get(url):
            write_collection(path_dst, content, L.settings)
            L.info(f'Refreshed collection: {path}')

    # Rebuild index for other HTML file requests.
    elif url.endswith(('/', '.html', '.htm')):
        L.info(f'Rebuild site for request URL: {path}')
        L.build()


def serve(options):
    L = Logya(options)
    L.build()
    # Make Logya object accessible to server.
    HTTPRequestHandler.L = L

    # Make sure absolute links work.
    base_url = f'http://{options.host}:{options.port}'
    env.globals['base_url'] = base_url

    # Avoid "OSError: [Errno 98] Address already in use"
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer((options.host, options.port), HTTPRequestHandler) as httpd:
        print(f'Serving on {base_url}')
        httpd.serve_forever()