"""
The program begins with setting a list of article link tags to the list of links
in the intial page. Then, it goes into a loop, finding a random article link tag
in the page, extracting the href attribute from it, printing the page, and
getting a new list of links from the extracted url.
"""
import requests
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())

# TODO: needs to add exceptions to make the program more robust.


def main():
    links = get_links('/wiki/Spectroscopy')
    while len(links) > 0:
        new_article = random.choice(links).attrs['href']
        print(new_article)
        links = get_links(new_article)


def get_links(article_url):
    r = requests.get('http://en.wikipedia.org{}'.format(article_url))
    bs = BeautifulSoup(r.text, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all(
        'a', {'href': re.compile('^(/wiki/)((?!:).)*$')})


if __name__ == '__main__':
    main()
