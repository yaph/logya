# -*- coding: utf-8 -*-
import ConfigParser

class Config:
    """Site configuration access."""

    def __init__(self, filename):
        """Create ConfigParser object read from the given file."""

        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open(filename))

    def get(self, section, var, required=False):
        try:
            val = self.config.get(section, var)
        except Exception:
            if required:
                raise Exception
            else:
                return False
        else:
            return val