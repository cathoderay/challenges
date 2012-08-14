#!/usr/bin/env python 
#
# File: challenge.py 
# Description: Americanas.com challenge
# Author: Ronald Kaiser <raios DOT catodicos AT gmail DOT com>
#

import requests 
from lxml.html import fromstring


def get_price(html, xpath):
    return fromstring(html).xpath(xpath)[0]


def get_html_from_url(url):
    return requests.get(url).text


if __name__ == "__main__":
    # Expected usage
    url = "http://www.americanas.com.br/produto/111359833/informatica/apple/macbook/macbook-pro-md101bz/a-intel-core-i5-led-13.3_-4gb-500gb-apple"
    xpath = "//p[@class='sale price']//span[@class='amount']/text()" 
    print get_price(get_html_from_url(url), xpath)
