# -*- coding: utf-8 -*-
from . import LogyaBaseTestCase


class TestConfig(LogyaBaseTestCase):

    def test_get(self):
        self.assertEqual(
            'http://localhost:8080', self.config.get('site', 'base_url'))
        self.assertIsNone(self.config.get('site', 'disqus_shortname'))

    def test_search_dict_list(self):
        self.assertEqual('post.html', self.config.search_dict_list(
            'templates', 'doc', 'content_type', 'template'))
        self.assertEqual('doc', self.config.search_dict_list(
            'templates', 'post.html', 'template', 'content_type'))

    def test_section(self):
        site = self.config.section('site')
        self.assertIn('base_url', site)
        self.assertIn('disqus_shortname', site)
