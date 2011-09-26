# -*- coding: utf-8 -*-
import os
from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer

class GeeklogServer(HTTPServer):

    def __init__(self, geeklog, address, port):
        self.geeklog = geeklog
        self.address = address
        self.port = port
        HTTPServer.__init__(self, (address, port), GeeklogHTTPRequestHandler)

    def serve(self):
        self.geeklog.init_env()
        os.chdir(self.geeklog.dir_dst)
        print 'Serving on http://%s:%s/' % (self.address, self.port)
        self.serve_forever()

class GeeklogHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        print "Requested resource: %s" % self.path
        self.server.geeklog.refresh_resource(self.path)
        SimpleHTTPRequestHandler.do_GET(self)
