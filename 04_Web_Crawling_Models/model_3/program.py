from website import Website
from crawler import Crawler


crawler = Crawler()

# site_data = [
#     ['O\'Reilly Media', 'http://oreilly.com',
#      'https://ssearch.oreilly.com/?q=', 'article.product-result',
#      'p.title a', True, 'h1', 'section#product-description'],
#     ['Reuters', 'http://reuters.com',
#      ''],
#     ['Brookings', 'http://www.brookings.edu', 'h1',
#      'div.post-body'],
#     ['New York Times', 'http://nytimes.com', 'h1',
#      'p.story-content'],
# ]

site_data = [
    ['O\'Reilly Media',
     'http://oreilly.com',
     'https://ssearch.oreilly.com/?q=',
     'article.product-result',
     'p.title a',
     True,
     'h1',
     'section#product-description']
]

sites = []
for row in site_data:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5],
                         row[6], row[7]))

    topics = ['python']
    for topic in topics:
        print("GETTING INFO ABOUT: " + topic)
        for target_site in sites:
            crawler.search(topic, target_site)
