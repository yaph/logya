# -*- coding: utf-8 -*-
import http.server
import socketserver

from pathlib import Path
from shutil import copyfile
from urllib.parse import unquote, urlparse

from logya.core import Logya
from logya.content import add_collections, read, read_all, write_collection
from logya.writer import DocWriter
from logya.util import paths, config, slugify

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
        print(f'Rebuild index for request URL: {url}')
        site_index.update(read_all(paths, config))
    if src_url not in site_index:
        print(f'No content or collection at: {src_url}')
        return

    content = site_index[src_url]
    path_dst = Path(paths.public, src_name, 'index.html')
    # Update content document
    if 'doc' in content:
        doc = read(content['path'], paths, config)

        # Update doc in collections if doc was changed before writing it to public.
        # FIXME move to function update_collection
        if content['path'].stat().st_mtime > path_dst.stat().st_mtime:
            for attr, collection in config['collections'].items():
                if attr not in doc:
                    continue
                for value in doc[attr]:
                    collection_url = f'/{collection["path"]}/{slugify(value.lower())}/'
                    if collection_url not in site_index:
                        site_index[collection_url] = {
                            'docs': [doc],
                            'title': value,
                            'path': collection['path'],  # FIXME avoid setting path, it is confusing because not a Path
                            'template': collection['template'],
                            'url': collection_url
                        }
                        continue
                    for idx, collection_doc in enumerate(site_index[collection_url]['docs']):
                        if doc['url'] == collection_doc['url']:
                            site_index[collection_url]['docs'][idx].update(doc)

        # Always write doc because of possible template changes.
        DocWriter(paths.public, L.template).write(doc, L.get_doc_template(doc))
        print(f'Refreshed doc at URL: {url}')
        return

    # Update collection page
    if 'docs' in content:
        write_collection(path_dst, content, L.template, config)
        print(f'Refreshed collection: {url}')


def serve(args):
    L.template.vars['base_url'] = f'http://{args.host}:{args.port}'
    with socketserver.TCPServer((args.host, args.port), HTTPRequestHandler) as httpd:
        print(f'Serving on {L.template.vars["base_url"]}')
        httpd.serve_forever()