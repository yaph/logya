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
            extension.set_module_name(modname)
            extension.set_directory(os.path.dirname(module.__file__))
            ext_type = extension.get_type()
            if ext_type not in self.extensions:
                self.extensions[ext_type] = []
            self.extensions[ext_type].append(extension)

    def get_by_type(self, name):
        return self.extensions[name]


class Extension():

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def process(self, arg):
        pass

    def set_directory(self, directory):
        """Set the property containing the extension source directory."""

        self.directory = directory

    def get_directory(self):
        """Get the property containing the extension source directory."""

        return self.directory

    def set_module_name(self, module_name):
        """Set the name of the extension module."""
        self.module_name = module_name

    def get_module_name(self):
        """Get the name of the extension module.

        The module name is used in unit tests.
        """
        return self.module_name

    def set_logya(self, logya):
        self.logya = logya

    def set_template(self, template):
        self.template = template
