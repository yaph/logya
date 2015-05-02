# -*- coding: utf-8 -*-
from logya.core import Logya
from logya.compat import execfile


class Run(Logya):
    """Run given script in Logya context."""

    def __init__(self, script):

        super(self.__class__, self).__init__()
        self.init_env()

        args = {'logya': self}
        execfile(script, args)
