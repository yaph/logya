# -*- coding: utf-8 -*-
import os
import logging
from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer

class LogyaServer(HTTPServer):

    def __init__(self, logya, address, port):
        self.logya = logya
        self.address = address
        self.port = port

        self.logya.init_env()
        log_file = os.path.join(self.logya.dir_current, 'server.log')
        logging.basicConfig(filename=log_file, level=logging.INFO)
        HTTPServer.__init__(self, (address, port), LogyaHTTPRequestHandler)

    def serve(self):
        os.chdir(self.logya.dir_dst)
        print 'Serving on http://%s:%s/' % (self.address, self.port)
        self.serve_forever()

class LogyaHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.info("Requested resource: %s" % self.path)
        logging.info(self.server.logya.refresh_resource(self.path))
        SimpleHTTPRequestHandler.do_GET(self)
