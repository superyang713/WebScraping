import requests
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())


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
