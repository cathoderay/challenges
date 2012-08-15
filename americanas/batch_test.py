import challenge


urls = open('challenge.in', 'r+')
xpath = "//p[@class='sale price']//span[@class='amount']/text()"
for url in urls.readlines():
    url = url.strip()
    print "Getting price from [%s]" % url
    print challenge.get_price(url, xpath)

