# -*- coding: utf-8 -*-
import shutil
import logging

from http.server import HTTPServer, SimpleHTTPRequestHandler
from os import chdir
from pathlib import Path
from urllib.parse import unquote, urlparse

from logya.core import Logya
from logya.content import add_collections, read, read_all, write_collection
from logya.writer import DocWriter
from logya.util import paths, config


class Serve(Logya):
    """Serve files from deploy directory."""

    def __init__(self, **kwargs):
        super(Serve, self).__init__()
        # If not passed as command arguments host and port are set to None.
        self.host = kwargs.get('host') or 'localhost'
        self.port = kwargs.get('port') or 8080
        Server(self).serve()

    def init_env(self):
        super(Serve, self).init_env()
        # Override base_url so links work locally.
        self.template.vars['base_url'] = f'http://{self.host}:{self.port}'
        # Set debug var to true in serve mode.
        self.template.vars['debug'] = True

    def build_index(self, mode='serve'):
        super(Serve, self).build_index(mode='serve')  # FIXME only do what is necessary
        self.site_index = read_all(paths, config)
        add_collections(self.site_index, config)

    def update_static(self, src):
        src_static = Path(self.dir_static, src)
        if src_static.is_file():
            dst_static = Path(self.dir_deploy, src)
            dst_static.parent.mkdir(exist_ok=True)
            if not dst_static.exists() or src_static.stat().st_mtime > dst_static.stat().st_mtime:
                shutil.copyfile(src_static, dst_static)
            return True

    def refresh_resource(self, url_path):
        """Refresh resource corresponding to given path.

        Static files are updated if necessary, documents are read, parsed and
        written to the corresponding destination in the deploy directory."""

        # FIXME Keep track of configuration changes first

        # Use only the actual path and ignore possible query params issue #3.
        src_url = unquote(urlparse(url_path).path)

        # If a static file is requested update it and return.
        if self.update_static(src_url.lstrip('/')):
            return

        # Try to get doc for requested URL.
        doc = None
        # FIXME Rebuild index if URL is unknown since new content may have been created.
        # if src_url not in self.site_index:
        #     self.build_index(mode='serve')
        if src_url not in self.site_index:
            logging.warning(f'No content or collection at: {src_url}')
            return

        content = self.site_index[src_url]
        # Update content document
        if 'doc' in content:
            doc = read(content['path'], paths, config)
            DocWriter(self.dir_deploy, self.template).write(doc, self.get_doc_template(doc))
            logging.info('Refreshed doc at URL: %s', src_url)
            return
        # Update collection page
        if 'docs' in content:
            path = Path(paths.public, src_url.lstrip('/'), 'index.html')
            write_collection(path, content, self.template, config)
            logging.info('Refreshed collection at URL: %s', src_url)


class Server(HTTPServer):
    """Logya HTTPServer based class to serve generated site."""

    def __init__(self, logya):
        """Initialize HTTPServer listening on the specified host and port."""

        self.logya = logya
        self.logya.init_env()
        self.logya.build_index()

        logging.basicConfig(level=logging.INFO)

        HTTPServer.__init__(
            self, (self.logya.host, self.logya.port), HTTPRequestHandler)

    def serve(self):
        """Serve static files from logya deploy directory."""

        chdir(self.logya.dir_deploy)
        print('Serving on http://{}:{}/'
              .format(self.logya.host, self.logya.port))
        self.serve_forever()


class HTTPRequestHandler(SimpleHTTPRequestHandler):
    """Logya SimpleHTTPRequestHandler based class to return resources."""

    def do_GET(self):
        """Return refreshed resource."""

        self.server.logya.refresh_resource(self.path)
        SimpleHTTPRequestHandler.do_GET(self)
