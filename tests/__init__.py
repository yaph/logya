# -*- coding: utf-8 -*-
import unittest


class LogyaBaseTestCase(unittest.TestCase):

    def setUp(self):
        self.config = {
            'site': {
                'base_url': 'http://localhost:8080'
            },
            'content': {
                'index': {'template': 'index.html'},
                'doc': {'template': 'page.html'},
                'rss': {'template': 'rss2.xml'}
            },
            'collections': {
                'tags': {'path': 'tags', 'template': 'index.html'},
                'shoptags': {'path': 'shop/tags'}
            }
        }
