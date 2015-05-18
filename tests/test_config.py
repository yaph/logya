# -*- coding: utf-8 -*-
from . import LogyaBaseTestCase

from logya import config


class TestConfig(LogyaBaseTestCase):


    def test_site(self):
        site = self.config['site']
        self.assertIn('base_url', site)

    def test_collections(self):
        self.assertIn('collections', self.config)

    def test_templates(self):
        self.assertIn('templates', self.config)

    def test_search_dict_list(self):
        self.assertEqual('post.html', config.search_dict_list(
            self.config, 'templates', 'doc', 'content_type', 'template'))
        self.assertEqual('doc', config.search_dict_list(
            self.config, 'templates', 'post.html', 'template', 'content_type'))

