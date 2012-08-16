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
        
    def test_get_price_from_html_happy_path(self):
        html = self.get_html('example.html')
        xpath = "//p[@class='sale price']//span[@class='amount']/text()"
        expected = "Por: R$ 3.999,00"
        result = challenge.get_raw_price(html, xpath)
        self.assertEqual(expected, result)

    def test_get_price_from_html_level_1_challenge(self):
        html = self.get_html('level1.html')
        xpath = "//div/text()"
        expected = 44.99
        result = challenge.clean_price(challenge.get_raw_price(html, xpath))
        self.assertEqual(expected, result)

    def test_detect_unavailable_product(self):
        html = self.get_html('unavailable.html')
        xpath = "//p[@class='sale price']//span[@class='amount']/text()"
        unv_xpath = "//div[@class='unavailProd']"
        expected = "Unavailable"
        result = challenge.get_raw_price(html, xpath, unv_xpath)
        self.assertEqual(expected, result)

    def test_cleaning_price_with_dot(self):
        raw_price = "Por: R$ 3.999,00"
        expected = 3999.0
        result = challenge.clean_price(raw_price)
        self.assertEqual(expected, result)

    def test_cleaning_price_without_dots(self):
        raw_price = "Por: R$ 42,42"
        expected = 42.42
        result = challenge.clean_price(raw_price)
        self.assertEqual(expected, result)

    def test_get_raw_price_should_return_empty_if_doesnt_find_xpath(self):
        html = self.get_html('example.html') 
        xpath = "//p[@class='love is all you need']"
        expected = ""
        result = challenge.get_raw_price(html, xpath)
        self.assertEqual(expected, result)

    def test_cleaning_price_should_not_throw_exception(self):
        raw_price = ""
        expected = ""
        result = challenge.clean_price(raw_price)
        self.assertEqual(expected, result)

    def test_return_empty_when_url_does_not_exist(self):
        url = "http://youaresobeautiful4242.com"
        expected = ""
        result = challenge.fetch_html_from_url(url)
        self.assertEqual(expected, result)

    def test_return_empty_if_redirected(self):
        url = "http://www.americanas.com.br/produto/spam_and_eggs"
        expected = ""
        result = challenge.fetch_html_from_url(url)
        self.assertEqual(expected, result)

    def test_get_cookie_and_redirect(self):
        #WARNING: this test can fail due to unavailability of url
        url = "http://hughes.sieve.com.br:9090/level2/"
        expected = "R$ 3.999,00"
        result = challenge.fetch_html_from_url(url, use_cookie=True)
        self.assertTrue(result.find(expected) > 0)
        

    #TODO: add more tests

if __name__ == "__main__":
    unittest.main()
