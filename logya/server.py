import http.server
import socketserver
from shutil import copyfile
from urllib.parse import unquote, urlparse

from logya.content import read, write_collection, write_page
from logya.core import Logya
from logya.template import env


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler based class to return resources."""

    L: Logya

    def __init__(self, *args):
        super().__init__(*args, directory=self.L.paths.public.as_posix())

    def do_GET(self):  # noqa: N802
        update_resource(self.path, self.L)
        super().do_GET()


def update_page(url: str, L: Logya) -> bool:
    """Update content or collection page."""

    if content := L.doc_index.get(url):
        path_rel = content['path'].relative_to(L.paths.content)
        content['doc'] = read(content['path'], path_rel, L.markdown_extensions)
        if L.collections:
            L.update_collections(content['doc'])
        # Always write doc because of possible template changes.
        write_page(L.paths.public, content['doc'])
        L.info(f'Refreshed doc: {url}')
        return True

    if content := L.collection_index.get(url):
        write_collection(L.paths.public, content)
        L.info(f'Refreshed collection: {url}')
        return True

    return False


def update_resource(path: str, L: Logya) -> None:
    """Update resource corresponding to given url.

    Resources that exist in the `static` directory are updated if they are newer than the destination file.
    For other HTML resources the whole `L.doc_index` is updated and the destination is newly written."""

    # Use only the actual path and ignore possible query params (see issue #3).
    url = unquote(urlparse(path).path)
    url_rel = url.lstrip('/')

    # If a static file is requested update it and return.
    src_static = L.paths.static.joinpath(url_rel)
    if src_static.is_file():
        dst_static = L.paths.public.joinpath(url_rel)
        dst_static.parent.mkdir(exist_ok=True)
        if not dst_static.exists() or src_static.stat().st_mtime > dst_static.stat().st_mtime:
            L.info(f'Update static resource: {dst_static}')
            copyfile(src_static, dst_static)
        return

    # Update content or collection existing in respective index.
    if update_page(url, L):
        return

    # Rebuild indexes for other HTML file requests and try again to update page in case of new content.
    if url.endswith(('/', '.html', '.htm')):
        L.info(f'Rebuild site for request URL: {url}')
        L.build()
        if not update_page(url, L):
            L.info(f'URL not found: {url}')


def serve(dir_site: str, verbose: bool, host: str, port: int, **kwargs) -> None:
    L = Logya(dir_site=dir_site, verbose=verbose)
    L.build()
    # Make Logya object accessible to server.
    HTTPRequestHandler.L = L

    # Make sure absolute links work.
    base_url = f'http://{host}:{port}'
    env.globals['base_url'] = base_url

    # Avoid "OSError: [Errno 98] Address already in use"
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer((host, port), HTTPRequestHandler) as httpd:
        print(f'Serving on {base_url}')
        httpd.serve_forever()
