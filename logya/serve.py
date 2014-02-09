# -*- coding: utf-8 -*-
import os
import shutil
import logging

from logya.core import Logya
from logya.compat import urlparse
from logya.compat import HTTPServer
from logya.compat import SimpleHTTPRequestHandler
from logya.writer import FileWriter, DocWriter


class Serve(Logya):
    """Serve files from deploy directory."""

    host = 'localhost'
    port = 8080

    def __init__(self, **kwargs):

        if 'host' in kwargs and kwargs['host']:
            self.host = kwargs['host']

        if 'port' in kwargs and kwargs['port']:
            self.port = kwargs['port']

        super(Serve, self).__init__()
        Server(self).serve()

    def init_env(self):
        super(Serve, self).init_env()
        # override base_url from config in templates
        base_url = 'http://%s:%d' % (self.host, self.port)
        self.template.add_var('base_url', base_url)

    def update_file(self, src, dst):
        """Copy source file to destination file if source is newer.

        Creates destination directory and file if they don't exist.
        """

        # make sure destination directory exists
        dir_dst = os.path.dirname(dst)
        if not os.path.exists(dir_dst):
            os.makedirs(dir_dst)

        if not os.path.isfile(dst):
            shutil.copy(src, dir_dst)
            return True

        if os.path.getmtime(src) > os.path.getmtime(dst):
            shutil.copyfile(src, dst)
            return True

        return False

    def refresh_resource(self, path):
        """Refresh resource corresponding to given path.

        Static files are updated if necessary, documents are read, parsed and
        written to the corresponding destination in the deploy directory."""

        # has to be done here too to keep track of configuration changes
        self.init_env()

        # if a file relative to static source is requested update it and return
        path_rel = path.lstrip('/')
        # use only the path component and ignore possible query params issue #3
        file_src = urlparse(os.path.join(self.dir_static, path_rel)).path
        if os.path.isfile(file_src):
            file_dst = os.path.join(self.dir_dst, path_rel)
            if self.update_file(file_src, file_dst):
                return "Copied file %s to %s" % (file_src, file_dst)
            return "src %s not newer than dest %s" % (file_src, file_dst)

        # newly build generated docs and indexes
        self.exec_bin()
        self.build_indexes(mode='serve')

        # try to get doc at path, regenerate it and return
        doc = None
        if path in self.docs_parsed:
            doc = self.docs_parsed[path]
        else:
            # if a path like /index.html is requested also try to find /
            alt_path = os.path.dirname(path)
            if not alt_path.endswith('/'):
                alt_path = '%s/' % alt_path
            if alt_path in self.docs_parsed:
                doc = self.docs_parsed[alt_path]

        if doc:
            docwriter = DocWriter(self.dir_dst, self.template)
            docwriter.write(doc, self.get_doc_template(doc))
            self.write_indexes()
            return "Refreshed doc at URL: %s" % path
        else:
            # try to refresh auto-generated index file
            index_paths = list(self.indexes.keys())
            path_normalized = path.strip('/')
            if path_normalized in index_paths:
                template = self.config.get_item(
                    'templates', 'index', 'content_type', 'template')
                if template:
                    self.write_index(FileWriter(), path_normalized, template)


class Server(HTTPServer):
    """Logya HTTPServer based class to serve generated site."""

    def __init__(self, logya):
        """Initialize HTTPServer listening on the specified host and port."""

        self.logya = logya
        self.logya.init_env()

        log_file = os.path.join(self.logya.dir_current, 'server.log')
        logging.basicConfig(filename=log_file, level=logging.INFO)

        HTTPServer.__init__(
            self, (self.logya.host, self.logya.port), HTTPRequestHandler)

    def serve(self):
        """Serve static files from logya deploy directory."""

        os.chdir(self.logya.dir_dst)
        print(('Serving on http://%s:%s/' % (self.logya.host, self.logya.port)))
        self.serve_forever()


class HTTPRequestHandler(SimpleHTTPRequestHandler):
    """Logya SimpleHTTPRequestHandler based class to return resources."""

    def do_GET(self):
        """Return refreshed resource."""

        logging.info("Requested resource: %s" % self.path)
        self.server.logya.refresh_resource(self.path)
        SimpleHTTPRequestHandler.do_GET(self)