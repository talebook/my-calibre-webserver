#!/usr/bin/python3
#-*- coding: UTF-8 -*-

import logging
import unittest

from lib.douban import DoubanBookApi


def ins():
    api = DoubanBookApi(u"0df993c66c0c636e29ecbb5344252a4a")
    api._to_calibre_meta = lambda r: r
    return api


class TestLibDouban(unittest.TestCase):
    def test_douban_meta(self):
        api = ins()
        books = api.get_books_by_title(u'三体')
        logging.error(books)
        self.assertTrue("abc" in books)


if __name__ == '__main__':
    unittest.main()
