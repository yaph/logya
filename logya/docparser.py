# -*- coding: utf-8 -*-
import os
import yaml
from datetime import datetime

class DocParser():
    """Class for parsing content documents."""

    def parse(self, filename):
        """Parse document and return a dictionary of header fields and body."""

        stat = os.stat(filename)
        f = open(filename, 'r')
        content = f.read()
        f.close()

        # extract YAML header and body
        pos1 = content.index('---')
        pos2 = content.index('---', pos1 + 1)
        header = content[pos1:pos2].strip()
        body = content[pos2+3:].strip()

        self.parsed = yaml.load(header)
        self.parsed['body'] = body

        # use file modification time if created is not set
        if 'created' not in self.parsed:
            self.parsed['created'] = datetime.fromtimestamp(stat.st_mtime)

        return self.parsed
