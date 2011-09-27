# -*- coding: utf-8 -*-
import pkgutil
from abc import ABCMeta, abstractmethod

class ExtensionLoader():

    def __init__(self):
        self.extensions = {}
        for importer, modname, is_pkg in pkgutil.iter_modules([__path__[0]]):
            module = importer.find_module(modname).load_module(modname)
            extension = module.main()
            ext_type = extension.get_type()
            if not self.extensions.has_key(ext_type):
                self.extensions[ext_type] = []
            self.extensions[ext_type].append(extension)

    def get_by_type(self, name):
        return self.extensions[name]

class Extension:

    __metaclass__ = ABCMeta

    @abstractmethod
    def process(self, arg):
        pass

    @abstractmethod
    def get_type(self):
        pass
