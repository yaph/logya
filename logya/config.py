# -*- coding: utf-8 -*-
import io
import yaml


class Config:
    """Site configuration access."""

    def __init__(self, filename):
        """Create config object read from the given file."""

        with io.open(filename, 'r', encoding='utf-8') as f:
            self.config = yaml.load(f)

    def get(self, section, key):
        return self.config[section].get(key, None)

    def search_dict_list(self, section, search, search_key, value_key):
        for item in self.config[section]:
            if search == item[search_key]:
                return item[value_key]

    def section(self, section):
        return self.config[section]
