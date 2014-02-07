# -*- coding: utf-8 -*-
import os
import yaml
import markdown

from datetime import datetime
from logya.compat import file_open as open


class DocParser():
    """Class for parsing content documents."""

    def parse(self, filename):
        """Parse document and return a dictionary of header fields and body."""

        stat = os.stat(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        if not content:
            return

        # extract YAML header and body
        pos1 = content.index('---')
        pos2 = content.index('---', pos1 + 1)
        header = content[pos1:pos2].strip()
        body = content[pos2 + 3:].strip()

        # parse body if not HTML/XML
        fext = os.path.splitext(filename)[1]
        if '.md' == fext or '.markdown' == fext:
            body = markdown.markdown(body.decode('utf-8'))

        self.parsed = yaml.load(header)
        self.parsed['body'] = body

        # use file modification time if created is not set
        if 'created' not in self.parsed:
            self.parsed['created'] = datetime.fromtimestamp(stat.st_mtime)

        return self.parsed
