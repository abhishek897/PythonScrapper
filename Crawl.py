import requests
import re

nreviews_re = {'com': re.compile('\d[\d,]+(?= customer review)'), 
               'co.uk':re.compile('\d[\d,]+(?= customer review)'),
               'de': re.compile('\d[\d\.]+(?= Kundenrezens\w\w)')}
no_reviews_re = {'com': re.compile('no customer reviews'), 
                 'co.uk':re.compile('no customer reviews'),
                 'de': re.compile('Noch keine Kundenrezensionen')}
print "5"

def get_number_of_reviews(asin=1433524767, country='com'):                                 
    print "1"
    url = 'http://www.amazon.{country}/product-reviews/{asin}'.format(country=country, asin=asin)
    print url
    html = requests.get(url).text
    print html
    try:
	print "2"
        return int(re.compile('\D').sub('',nreviews_re[country].search(html).group(0)))
	
    except:
        if no_reviews_re[country].search(html):
            print "3"
        else:
            print "4"  # to distinguish from 0, and handle more cases if necessary

if __name__ == '__main__':
    get_number_of_reviews(asin=1433524767, country='com')