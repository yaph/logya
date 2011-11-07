# -*- coding: utf-8 -*-
import os
import shutil
import logging
from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer
from logya import Logya
from docreader import DocReader
from docparser import DocParser
from writer import DocWriter

class Serve(Logya):
    """Serve files from deploy directory."""

    def __init__(self, **kwargs):

        host = 'localhost'
        if kwargs.has_key('host') and kwargs['host']:
            host =  kwargs['host']

        port = 8080
        if kwargs.has_key('port') and kwargs['port']:
            port =  kwargs['port']

        super(self.__class__, self).__init__()
        Server(self, host, port).serve()

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

        self.init_env()

        # if a file relative to static source is requested update it and return
        path_rel = path.lstrip('/')
        file_src = os.path.join(self.dir_static, path_rel)

        if os.path.isfile(file_src):
            file_dst = os.path.join(self.dir_dst, path_rel)
            if self.update_file(file_src, file_dst):
                return "Copied file %s to %s" % (file_src, file_dst)
            return "Source %s is not newer than destination %s" % (file_src, file_dst)

        # find doc that corresponds to path, regenerate it and return
        docs = DocReader(self.dir_content, DocParser()).get_docs()
        for doc in docs:
            if not doc.has_key('url'):
                continue
            url = doc['url']
            # be forgiving about trailing slashes when checking for requested doc
            if path.rstrip('/') == url.rstrip('/'):
                dw = DocWriter(self.dir_dst, self.template)
                dw.write(doc)
                return "Refreshed doc at URL: %s" % url

class Server(HTTPServer):
    """Logya HTTPServer based class to serve generated site."""

    def __init__(self, logya, address, port):
        """Initialize HTTPServer listening on the specified address and port."""

        self.logya = logya
        self.address = address
        self.port = port

        self.logya.init_env()
        log_file = os.path.join(self.logya.dir_current, 'server.log')
        logging.basicConfig(filename=log_file, level=logging.INFO)
        HTTPServer.__init__(self, (address, port), HTTPRequestHandler)

    def serve(self):
        """Serve static files from logya deploy directory."""

        os.chdir(self.logya.dir_dst)
        print 'Serving on http://%s:%s/' % (self.address, self.port)
        self.serve_forever()

class HTTPRequestHandler(SimpleHTTPRequestHandler):
    """Logya SimpleHTTPRequestHandler based class to return resources."""

    def do_GET(self):
        """Return refreshed resource."""

        logging.info("Requested resource: %s" % self.path)
        logging.info(self.server.logya.refresh_resource(self.path))
        SimpleHTTPRequestHandler.do_GET(self)