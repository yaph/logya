# -*- coding: utf-8 -*-
import os
import logging
from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer

class GeeklogServer(HTTPServer):

    def __init__(self, geeklog, address, port):
        self.geeklog = geeklog
        self.address = address
        self.port = port

        self.geeklog.init_env()
        log_file = os.path.join(self.geeklog.dir_current, 'server.log')
        logging.basicConfig(filename=log_file, level=logging.INFO)
        HTTPServer.__init__(self, (address, port), GeeklogHTTPRequestHandler)

    def serve(self):
        os.chdir(self.geeklog.dir_dst)
        print 'Serving on http://%s:%s/' % (self.address, self.port)
        self.serve_forever()

class GeeklogHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.info("Requested resource: %s" % self.path)
        logging.info(self.server.geeklog.refresh_resource(self.path))
        SimpleHTTPRequestHandler.do_GET(self)
