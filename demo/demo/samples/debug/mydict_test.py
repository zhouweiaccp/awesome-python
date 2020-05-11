#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from mydict import DDict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = DDict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = DDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = DDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = DDict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = DDict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()

