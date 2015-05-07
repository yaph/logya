# -*- coding: utf-8 -*-
import os
import shutil
from pkg_resources import resource_filename
from logya.core import Logya


class Create(Logya):
    """Create a basic template for generating a Web site with Logya."""

    def __init__(self, name):

        super(self.__class__, self).__init__()
        src = resource_filename(__name__, 'sites/starter')
        dst = os.path.join(self.dir_site, name)
        shutil.copytree(src, dst)
