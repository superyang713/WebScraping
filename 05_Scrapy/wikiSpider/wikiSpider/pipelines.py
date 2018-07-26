from datetime import datetime
from string import whitespace

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from wikiSpider.items import Article


class WikispiderPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, Article):
            item['lastUpdated'] = item['lastUpdated'].replace(
                'This page was last edited on', ''
            )
            item['lastUpdated'] = item['lastUpdated'].strip()
            item['lastUpdated'] = datetime.strptime(
                item['lastUpdated'], '%d %B %Y, at %H:%M.'
            )
            item['text'] = [line for line in item['text']
                            if line not in whitespace]
            item['text'] = ''.join(item['text'])
            return item
