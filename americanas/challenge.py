#!/usr/bin/env python 
#
# File: challenge.py 
# Description: Americanas.com challenge
# Author: Ronald Kaiser <raios DOT catodicos AT gmail DOT com>
#

import sys

import requests 
from lxml.html import fromstring


def get_raw_price(html, xpath):
    return fromstring(html).xpath(xpath)[0]


def clean_price(raw_price):
    pass


def fetch_html_from_url(url):
    return requests.get(url).text


if __name__ == "__main__":
    xpath = "//p[@class='sale price']//span[@class='amount']/text()" 
    if len(sys.argv) > 1:
        print get_raw_price(fetch_html_from_url(sys.argv[1]), xpath)
    else:
        print "Usage: ./challenge.py url"
