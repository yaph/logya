# -*- coding: utf-8 -*-
import unittest


class LogyaBaseTestCase(unittest.TestCase):

    def setUp(self):
        self.config = {
            'site': {
                'base_url': 'http://localhost:8080'
            },
            'templates': [
                {'content_type': 'index', 'template': 'index.html'},
                {'content_type': 'doc', 'template': 'post.html'},
                {'content_type': 'rss', 'template': 'rss2.xml'}
            ],
            'indexes': [
                {'var': 'tags', 'path': 'tags'}
            ]
        }
