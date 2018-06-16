from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from wikiSpider.items import Article


class ArticleSpider(CrawlSpider):
    name = 'articleItems'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']
    rules = [
        Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'), callback='parse_items',
             follow=True)
    ]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('h1::text').extract_first()
        article['text'] = response.xpath(
            '//div[@id="mw-content-text"]//text()').extract()
        article['lastUpdated'] = response.css(
            'li#footer-info-lastmod::text').extract_first()
        return article
