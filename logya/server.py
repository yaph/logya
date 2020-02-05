# -*- coding: utf-8 -*-
# TODOs
# Watch for changes in `static` and `content` dirs.
# New and changed `static` files are copied to `public`.
# New files in `content` that have an allowed extension and not set to `noindex` result in a full rebuild of the index.
# In `do_GET` update `content` and generated `index` pages on every request.
import http.server
import socketserver

from multiprocessing import Process
from pathlib import Path
from shutil import copyfile
from urllib.parse import unquote, urlparse

from watchgod import watch

from logya.core import Logya
from logya.content import add_collections, read, read_all, write_collection
from logya.writer import DocWriter
from logya.util import paths, config


site_index = read_all(paths, config)
add_collections(site_index, config)
L = Logya()
L.init_env()
L.build_index()
L.template.vars['debug'] = True


class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """SimpleHTTPRequestHandler based class to return resources."""

    def __init__(self, *args):
        super(HTTPRequestHandler, self).__init__(*args, directory=paths.public.as_posix())

    def do_GET(self):
        update_resource(self.path)
        super(HTTPRequestHandler, self).do_GET()


def update_resource(url):
    """Update resource corresponding to given url.

    Resources that exist in the `static` directory are updated if they are newer than the destination file.
    For other HTML resources the whole `site_index` is updated and the destination is newly written."""

    # Use only the actual path and ignore possible query params issue #3.
    src_url = unquote(urlparse(url).path)
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

    # Rebuild index for HTML file requests.
    if url.endswith(('/', '.html', '.htm')):
        site_index.update(read_all(paths, config))
    if src_url not in site_index:
        print(f'No content or collection at: {src_url}')
        return

    content = site_index[src_url]
    path_dst = Path(paths.public, src_name, 'index.html')
    # Update content document
    if 'doc' in content:
        doc = read(content['path'], paths, config)

        # Update collections document occurs in, if doc was changed.
        # FIXME instead of iterating site_index iterate doc collections
        if content['path'].stat().st_mtime > path_dst.stat().st_mtime:
            for i_url, i_content in site_index.items():
                if 'docs' not in i_content:
                    continue
                for idx, i_doc in enumerate(i_content['docs']):
                    if url == i_doc['url']:
                        site_index[i_url]['docs'][idx] = doc

        # Always write doc because of possible template changes.
        DocWriter(paths.public, L.template).write(doc, L.get_doc_template(doc))
        print(f'Refreshed doc at URL: {url}')
        return

    # Update collection page
    if 'docs' in content:
        write_collection(path_dst, content, L.template, config)
        print(f'Refreshed collection: {url}')


def watch_content():
    for changes in watch(paths.content):
        change, abs_path = list(changes)[0]
        if 'added' == change.name:
            print('Added: ' + abs_path)
        elif 'deleted' == change.name:
            print('Deleted: ' + abs_path)


def watch_static():
    for changes in watch(paths.content):
        change, abs_path = list(changes)[0]
        if 'added' == change.name:
            print('Added: ' + abs_path)
        elif 'modified' == change.name:
            print('Modified: ' + abs_path)
        elif 'deleted' == change.name:
            print('Deleted: ' + abs_path)


def serve_public(args):
    L.template.vars['base_url'] = f'http://{args.host}:{args.port}'
    with socketserver.TCPServer((args.host, args.port), HTTPRequestHandler) as httpd:
        print(f'Serving on {L.template.vars["base_url"]}')
        httpd.serve_forever()


def serve(args):
    Process(target=serve_public, args=(args,)).start()
    Process(target=watch_content).start()
    Process(target=watch_static).start()