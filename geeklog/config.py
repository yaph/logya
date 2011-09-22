# -*- coding: utf-8 -*-
import ConfigParser

def get(file_name):
    """Get the configuration object read from the given file."""

    config = ConfigParser.ConfigParser()
    config.readfp(open(file_name))
    return config
