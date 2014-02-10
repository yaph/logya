# -*- coding: utf-8 -*-
from base import LogyaBaseTestCase


class TestConfig(LogyaBaseTestCase):

    def test_get(self):
        self.assertEqual(
            'http://localhost:8080', self.config.get('site', 'base_url'))
        self.assertIsNone(self.config.get('site', 'disqus_shortname'))

    def test_get_item(self):
        self.assertEqual('post.html', self.config.get_item(
            'templates', 'doc', 'content_type', 'template'))
        self.assertEqual('doc', self.config.get_item(
            'templates', 'post.html', 'template', 'content_type'))

    def test_get_section(self):
        site = self.config.get_section('site')
        self.assertIn('base_url', site)
        self.assertIn('disqus_shortname', site)