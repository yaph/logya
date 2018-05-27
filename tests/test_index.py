# -*- coding: utf-8 -*-
from . import LogyaBaseTestCase
from logya.core import get_collection_var


class TestIndex(LogyaBaseTestCase):

    def test_get_collection_var(self):
        collection_index = {
            v['path']: k for k, v in self.config['collections'].items()}

        testdata = [
            {'input': 'post', 'expected': None},
            {'input': 'tags', 'expected': None},
            {'input': 'tags/tag1', 'expected': 'tags'},
            {'input': 'tags/tag-all', 'expected': 'tags'},
            {'input': 'tags/tag2', 'expected': 'tags'},
            {'input': 'shop/tags/tag1', 'expected': 'shoptags'},
            {'input': 'shop/tags/tag-all', 'expected': 'shoptags'},
            {'input': 'shop/tags/tag2', 'expected': 'shoptags'}
        ]

        for data in testdata:
            self.assertEqual(
                data['expected'],
                get_collection_var(data['input'], collection_index))
