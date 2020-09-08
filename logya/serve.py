# -*- coding: utf-8 -*-
import os
import shutil
import logging

from logya.core import Logya
from logya.compat import unquote, urlparse
from logya.compat import HTTPServer
from logya.compat import SimpleHTTPRequestHandler
from logya.writer import DocWriter


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

        # Override base_url so resources linked with absolute internal URLs
        # in templates are served locally.
        base_url = 'http://{}:{:d}'.format(self.host, self.port)
        self.template.vars['base_url'] = base_url

        # Set debug var to true in serve mode.
        self.template.vars['debug'] = True

    def update_file(self, src, dst):
        """Copy source file to destination file if source is newer.

        Creates destination directory and file if they don't exist.
        """

        # Make sure destination directory exists.
        dir_deploy = os.path.dirname(dst)
        if not os.path.exists(dir_deploy):
            os.makedirs(dir_deploy)

        if not os.path.isfile(dst):
            shutil.copy(src, dir_deploy)
            return True

        if os.path.getmtime(src) > os.path.getmtime(dst):
            shutil.copyfile(src, dst)
            return True

        return False

    def refresh_resource(self, path):
        """Refresh resource corresponding to given path.

        Static files are updated if necessary, documents are read, parsed and
        written to the corresponding destination in the deploy directory."""

        # Keep track of configuration changes.
        self.init_env()

        # If a static file is requested update it and return.
        path_rel = path.lstrip('/')
        # Use only the URL path and ignore possible query params issue #3.
        src = unquote(urlparse(os.path.join(self.dir_static, path_rel)).path)

        if os.path.isfile(src):
            dst = os.path.join(self.dir_deploy, path_rel)

            if self.update_file(src, dst):
                logging.info('Copied file %s to %s', src, dst)
                return

            logging.info('%s not newer than %s', src, dst)
            return

        # Newly build generated docs and index for HTML page requests.
        if path.endswith(('/', '.html', '.htm')):
            self.build_index(mode='serve')

        # Try to get doc at path, regenerate it and return.
        doc = None
        if path in self.docs:
            doc = self.docs[path]
        else:
            # If a path like /index.html is requested also try to find /.
            alt_path = os.path.dirname(path)
            if not alt_path.endswith('/'):
                alt_path = '{}/'.format(alt_path)
            if alt_path in self.docs:
                doc = self.docs[alt_path]

        if doc:
            docwriter = DocWriter(self.dir_deploy, self.template)
            docwriter.write(doc, self.get_doc_template(doc))
            self.write_index_files()
            logging.info('Refreshed doc at URL: %s', path)
        else:
            # Try to refresh auto-generated index file.
            path_index = path.strip('/')
            if path_index in self.index:
                self.write_index(path_index, self.index[path_index])


class Server(HTTPServer):
    """Logya HTTPServer based class to serve generated site."""

    def __init__(self, logya):
        """Initialize HTTPServer listening on the specified host and port."""

        self.logya = logya
        self.logya.init_env()

        logging.basicConfig(level=logging.INFO)

        HTTPServer.__init__(
            self, (self.logya.host, self.logya.port), HTTPRequestHandler)

    def serve(self):
        """Serve static files from logya deploy directory."""

        os.chdir(self.logya.dir_deploy)
        print('Serving on http://{}:{}/'
              .format(self.logya.host, self.logya.port))
        self.serve_forever()


class HTTPRequestHandler(SimpleHTTPRequestHandler):
    """Logya SimpleHTTPRequestHandler based class to return resources."""

    def do_GET(self):
        """Return refreshed resource."""

        logging.info('Requested resource: %s', self.path)
        self.server.logya.refresh_resource(self.path)
        SimpleHTTPRequestHandler.do_GET(self)
