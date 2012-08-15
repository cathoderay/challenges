#!/usr/bin/env python 
#
# File: challenge.py 
# Description: Americanas.com challenge
# Author: Ronald Kaiser <raios DOT catodicos AT gmail DOT com>
#

import re
import sys

import requests 
from lxml.html import fromstring


def get_raw_price(html, xpath):
    try:
        return fromstring(html).xpath(xpath)[0]
    except Exception:
        return ''


def clean_price(raw_price):
    try:
        return float(
                re.search('.*R\$ ([0-9.,]+).*', raw_price).group(1).
                 replace('.', '').
                  replace(',', '.'))
    except Exception:
        return raw_price


def fetch_html_from_url(url):
    return requests.get(url).text


def get_price(url, xpath):
    return clean_price(
            get_raw_price(
             fetch_html_from_url(sys.argv[1]), 
             xpath))


if __name__ == "__main__":
    xpath = "//p[@class='sale price']//span[@class='amount']/text()" 
    if len(sys.argv) > 1:
        print get_price(sys.argv[1], xpath)
    else:
        print "Usage: ./challenge.py url"
