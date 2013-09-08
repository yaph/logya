# -*- coding: utf-8 -*-
from logya.core import Logya


class Test(Logya):
    """Test new features."""

    def __init__(self, **kwargs):

        super(self.__class__, self).__init__()
        self.init_env()

        from logya.ext import ExtensionLoader
        el = ExtensionLoader()
        print(el.get_by_type('doc'))
        print(el.get_by_type('index'))
