"""
Collecting data across the entire wiki website.
"""

import requests
from bs4 import BeautifulSoup
import re
import time


def main():
    get_all_wiki_links('/wiki/haha')


def get_all_wiki_links(page_url):
    """
    It will map the entire wikipedia website. However, since wiki is a huge
    website, and this function is recursive, it will not be able to map the
    whole site. Instead, this is just an example of how to write a simple
    crawler.
    """
    pages = set()
    # if page_url is an empty string, it will start from the homepage.
    r = requests.get('http://en.wikipedia.org{}'.format(page_url))
    bs = BeautifulSoup(r.text, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Continuing.')

    time.sleep(5)

    for link in bs.find_all('a', {'href': re.compile('^(/wiki/)((?!:).)*$')}):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # We have encountered a new page.
                new_page = link.attrs['href']
                print('-' * 20)
                print(new_page)
                pages.add(new_page)
                get_all_wiki_links(new_page)
    return pages


if __name__ == '__main__':
    main()
