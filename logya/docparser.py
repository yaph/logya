# -*- coding: utf-8 -*-
import os
import re
import StringIO
import httplib
from datetime import datetime

class FakeSocket:
    """Code copied from pypy / lib-python / 2.7.1 / test / test_httplib.py
    See
    https://github.com/pypy/pypy/raw/cc0b90a9458a4d8146e7ff7ad757d63a7a97a535/lib-python/2.7.1/test/test_httplib.py
    http://pypy.org/
    """

    def __init__(self, text, fileclass=StringIO.StringIO):
        self.text = text
        self.fileclass = fileclass
        self.data = ''

    def makefile(self, mode, bufsize=None):
        if mode != 'r' and mode != 'rb':
            raise httplib.UnimplementedFileMode()
        return self.fileclass(self.text)

class FileResponse(httplib.HTTPResponse):
    """See
    http://svn.python.org/view/python/trunk/Lib/httplib.py?view=markup
    """

    def __init__(self, file):
        httplib.HTTPResponse.__init__(self, FakeSocket(open(file).read()))

    def _read_status(self):
        [version, status, reason] = 'HTTP/1.0 200 OK'.split(None, 2)
        return version, status, reason

class DocParser():

    multi_value_fields = ['scripts', 'styles', 'tags']

    # TODO make this callable from extensions
    def add_multi_value_field(self, name):
        """Add given name to the list of multi value document fields."""

        self.multi_value_fields.append(name)

    def parse(self, file):
        """Parse document and return a dictionary of header fields and body."""

        stat = os.stat(file)
        self.response = FileResponse(file)
        self.response.begin()
        self.parsed = {}
        for field, val in self.response.getheaders():
            if val is not None:
                if field in self.multi_value_fields:
                    self.parsed[field] = re.split(',\s*', val)
                else:
                    self.parsed[field] = val

        # override created time with file modification time if not set
        if not self.parsed.has_key('created'):
            self.parsed['created'] = datetime.fromtimestamp(stat.st_mtime).isoformat()

        self.parsed['body'] = self.response.read()
        return self.parsed