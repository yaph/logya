# -*- coding: utf-8 -*-
import yaml


class Config:
    """Site configuration access."""

    def __init__(self, filename):
        """Create config object read from the given file."""

        with open(filename, 'r') as f:
            self.config = yaml.load(f)

    def get(self, section, key):
        return self.config[section].get(key, None)

    def get_item(self, section, search, search_key, value_key):
        for i in self.config[section]:
            if search == i[search_key]:
                return i[value_key]

    def get_section(self, section):
        return self.config[section]
