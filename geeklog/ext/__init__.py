# -*- coding: utf-8 -*-
import os
import pkgutil
from abc import ABCMeta, abstractmethod

class ExtensionLoader():

    def __init__(self):
        self.extensions = {}
        for importer, modname, is_pkg in pkgutil.iter_modules([__path__[0]]):
            module = importer.find_module(modname).load_module(modname)
            extension = module.main()
            extension.set_directory(os.path.dirname(module.__file__))
            ext_type = extension.get_type()
            if not self.extensions.has_key(ext_type):
                self.extensions[ext_type] = []
            self.extensions[ext_type].append(extension)

    def get_by_type(self, name):
        return self.extensions[name]

class Extension:

    __metaclass__ = ABCMeta

    def set_directory(self, directory):
        """Set the property containing the extension source directory."""

        self.directory = directory

    def get_directory(self):
        """Get the property containing the extension source directory."""

        return self.directory

    def set_geeklog(self, geeklog):
        self.geeklog = geeklog

    def set_template(self, template):
        self.template = template

    @abstractmethod
    def process(self, arg):
        pass

    @abstractmethod
    def get_type(self):
        pass
