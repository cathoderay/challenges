from challenge import get_price
 

def get_yes_link(r):
    from lxml import html
    import requests
    xpath = "//a[contains(text(), 'Sim')]/@href"
    subpath = html.fromstring(r.text).xpath(xpath)[0]
    url = "http://hughes.sieve.com.br:9090%s" % subpath
    return requests.get(url).content


url = "http://hughes.sieve.com.br:9090/level3/"
xpath = "//p/text()"
print get_price(url, xpath, after_fetch=get_yes_link)
