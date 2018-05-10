from website import Website
from crawler import Crawler


reuters = Website('Reuters', 'https://www.reuters.com', '^(/article/)', False,
                  'h1', 'div.body_1gnLA')
crawler = Crawler(reuters)
crawler.crawl()
