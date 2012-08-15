#!/usr/bin/env python
#
# File: test.py
# Description: challenge.py tests
# Author: Ronald Kaiser <raios DOT catodicos AT gmail DOT com>
#

import os
import unittest

import challenge


EXAMPLES_PATH = os.path.join('examples')


class ChallengeTest(unittest.TestCase):
    def get_html(self, filename):
        """Kind of a requests mock"""
        path = os.path.join(EXAMPLES_PATH, filename)
        return open(path, 'r').read()
        
    def test_get_price_from_html(self):
        html = self.get_html('example.html')
        xpath = "//p[@class='sale price']//span[@class='amount']/text()"
        result = challenge.get_raw_price(html, xpath)
        expected = "Por: R$ 3.999,00"
        self.assertEqual(expected, result)

    def test_cleaning_price(self):
        raw_price = "Por: R$ 3.999,00"
        expected = "3999.0"
        self.assertEqual(expected, challenge.clean_price(raw_price))


    #TODO: add more tests
       
if __name__ == "__main__":
    unittest.main()
