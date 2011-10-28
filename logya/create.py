# -*- coding: utf-8 -*-
import os
import shutil
from logya import Logya

class Create(Logya):
    """Create a basic template for generating a Web site with Logya."""

    def __init__(self, name):

        super(self.__class__, self).__init__()
        src = os.path.join(self.dir_src, 'sites', 'docs')
        dst = os.path.join(self.dir_current, name)
        shutil.copytree(src, dst)