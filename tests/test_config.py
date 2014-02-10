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

    def test_items(self):
        site = self.config.items('site')
        self.assertEqual(2, len(site))
        keys = [t[0] for t in site]
        self.assertIn('base_url', keys)
        self.assertIn('disqus_shortname', keys)