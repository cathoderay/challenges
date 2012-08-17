from challenge import get_price
 

def get_yes_link(r):
    from lxml import html
    import requests
    xpath = "//a[contains(text(), 'Sim')]/@href"
    subpath = html.fromstring(r.text).xpath(xpath)[0]
    url = "http://hughes.sieve.com.br:9090%s" % subpath
    headers = {'user-agent': 'Opera/9.99 (X11; U; sk)'}
    g =  requests.get(url, headers=headers)
    # yes, i agree it's not elegant, =P
    return requests.get('http://hughes.sieve.com.br:9090/level3/', headers=headers, cookies=g.cookies).text


url = "http://hughes.sieve.com.br:9090/level3/"
xpath = "//p/text()"
print get_price(url, xpath, use_cookie=True, after_fetch=get_yes_link)
