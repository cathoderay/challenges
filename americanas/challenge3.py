from challenge import get_price
 
url = "http://hughes.sieve.com.br:9090/level2/"
xpath = "//div/text()"
print get_price(url, xpath)
