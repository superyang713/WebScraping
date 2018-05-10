from website import Website
from crawler import Crawler


crawler = Crawler()

site_data = [
    ['O\'Reilly Media', 'http://oreilly.com', 'h1',
     'section#product-description'],
    ['Reuters', 'http://reuters.com', 'h1',
     'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu', 'h1',
     'div.post-body'],
    ['New York Times', 'http://nytimes.com', 'h1',
     'p.story-content'],
]

websites = []
for row in site_data:
    websites.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(websites[0], 'http://shop.oreilly.com/product/'
              '0636920028154.do')
crawler.parse(websites[1], 'http://www.reuters.com/article/'
              'us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(websites[2], 'https://www.brookings.edu/blog/techtank/'
              '2016/03/01/idea-to-retire-old-method-of-policy-education/')
crawler.parse(websites[3], 'https://www.nytimes.com/2018/01/'
              '28/business/energy-environment/oil-bomm.html')
