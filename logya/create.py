# -*- coding: utf-8 -*-
import os
import shutil
import sys
from pkg_resources import resource_filename
from logya.core import Logya


class Create(Logya):
    """Create a basic template for generating a Web site with Logya."""

    def __init__(self, name, site):

        super(self.__class__, self).__init__()

        target = os.path.join(self.dir_site, name)
        if os.path.exists(target):
            print('Error: The directory "{}" already exists. Please remove it or create your project in another location.'.format(target))
            sys.exit(1)

        try:
            source = resource_filename(__name__, 'sites/' + site)
        except KeyError:
            print('The site "{}" is not installed.'.format(site))
        else:
            shutil.copytree(source, target)
