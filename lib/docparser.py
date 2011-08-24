import re
import StringIO
import httplib

class FakeSocket:
    '''Code copied from pypy / lib-python / 2.7.1 / test / test_httplib.py
    See
    https://github.com/pypy/pypy/raw/cc0b90a9458a4d8146e7ff7ad757d63a7a97a535/lib-python/2.7.1/test/test_httplib.py
    http://pypy.org/
    '''
    def __init__(self, text, fileclass=StringIO.StringIO):
        self.text = text
        self.fileclass = fileclass
        self.data = ''

    def makefile(self, mode, bufsize=None):
        if mode != 'r' and mode != 'rb':
            raise httplib.UnimplementedFileMode()
        return self.fileclass(self.text)


class FileResponse(httplib.HTTPResponse):
    '''See
    http://svn.python.org/view/python/trunk/Lib/httplib.py?view=markup
    '''
    def __init__(self, filename):
        f = open(filename)
        httplib.HTTPResponse.__init__(self, FakeSocket(f.read()))

    def _read_status(self):
        [version, status, reason] = 'HTTP/1.0 200 OK'.split(None, 2)
        return version, status, reason


class DocParser():
    def __init__(self, filename):
        self.response = FileResponse(filename)
        self.response.begin()

    def getfields(self, name):
        return re.split(',\s*', self.getheader(name))

    def getbody(self):
        return self.response.read()

    def getheader(self, name, default=None):
        return self.response.getheader(name, default)

    def getscripts(self):
        return self.getfields('scripts')

    def getstyles(self):
        return self.getfields('styles')
