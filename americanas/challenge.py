#!/usr/bin/env python 
#
# File: challenge.py 
# Description: Americanas.com challenge
# Author: Ronald Kaiser <raios DOT catodicos AT gmail DOT com>
#

# TODO: change structure to support short circuit
# TODO: refactoring


import re
import sys

import requests 
from lxml.etree import XPathEvalError
from lxml.html import fromstring


def get_raw_price(html, xpath, unv_xpath=None):
    try:
        xml = fromstring(html)
        if unv_xpath != None and \
           len(xml.xpath(unv_xpath)) > 0:
            return "Unavailable"
        return xml.xpath(xpath)[0]
    except XPathEvalError:
        print "Invalid Xpath."
    except Exception, e:
        print "Can't find price in html."
    return ""


def clean_price(raw_price):
    try:
        return float(
                re.search('.*R\$ ([0-9.,]+).*', raw_price).group(1)
                .replace('.', '')
                .replace(',', '.'))
    except Exception:
        return raw_price


def redirected_to_home(r):
    return len(r.history) > 0 and \
           str(r.history[0].status_code).startswith('3') and \
           r.history[0].headers['location'].lower() == "http://www.americanas.com.br/"


def fetch_html_from_url(url, use_cookie=False, after_fetch=None):
    #TODO: too large string =(
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.77 Safari/537.1'}
    try:
        r = requests.get(url, headers=headers)
        if use_cookie:
            r = requests.get(url, headers=headers, cookies=r.cookies)
        if redirected_to_home(r):
            print "Redirect to home."
            return ""
    except Exception, e:
        print "Can't fetch html from url. %s" % e
        return ""
    if after_fetch:
        return after_fetch(r)
    return r.text


def get_price(url, xpath, unv_xpath=None, use_cookie=False, after_fetch=None):
    return clean_price(
            get_raw_price(
             fetch_html_from_url(url, use_cookie, after_fetch),
             xpath,
             unv_xpath))


if __name__ == "__main__":
    xpath = "//p[@class='sale price']//span[@class='amount']/text()" 
    unv_xpath = "//div[@class='unavailProd']"
    if len(sys.argv) > 1:
        print get_price(url=sys.argv[1], 
                        xpath=xpath, 
                        unv_xpath=unv_xpath)
    else:
        print "Usage: ./challenge.py url"
