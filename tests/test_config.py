# -*- coding: utf-8 -*-
from . import LogyaBaseTestCase


class TestConfig(LogyaBaseTestCase):


    def test_site(self):
        site = self.config['site']
        self.assertIn('base_url', site)

    def test_collections(self):
        self.assertIn('collections', self.config)

    def test_content(self):
        self.assertIn('content', self.config)
