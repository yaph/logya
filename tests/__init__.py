# -*- coding: utf-8 -*-
import unittest

from mock import patch
from logya.config import Config


def _mock_config(mock, config):
    mock.config = config


class LogyaBaseTestCase(unittest.TestCase):

    def setUp(self):
        self.patch = patch.object(Config, '__init__', _mock_config)
        self.patch.start()
        self.config = Config({
            'site': {
                'base_url': 'http://localhost:8080',
                'disqus_shortname': None,
            },
            'templates': [
                {'content_type': 'index', 'template': 'index.html'},
                {'content_type': 'doc', 'template': 'post.html'}
            ],
            'indexes': [
                {'var': 'tags', 'path': 'tags'}
            ]
        })

    def tearDown(self):
        self.patch.stop()
