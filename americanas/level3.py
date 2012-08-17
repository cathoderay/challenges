from challenge import get_price
 

def get_yes_link(r):
    from lxml import html
    import requests
    xpath = "//a[contains(text(), 'Sim')]/@href"
    subpath = html.fromstring(r.text).xpath(xpath)[0]
    url = "http://hughes.sieve.com.br:9090%s" % subpath
    g = requests.get(url)
    # yes, i agree it's not elegant, =P
    # TODO: check how to treat response headers properly, e.g. Set-Cookie:18=+; Path=/
    return requests.get('http://hughes.sieve.com.br:9090/level3/', cookies=g.cookies).text


url = "http://hughes.sieve.com.br:9090/level3/"
xpath = "//p/text()"
print get_price(url, xpath, after_fetch=get_yes_link)
