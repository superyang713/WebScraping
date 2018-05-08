"""
The program begins with setting a list of article link tags to the list of links
in the intial page. Then, it goes into a loop, finding a random article link tag
in the page, extracting the href attribute from it, printing the page, and
getting a new list of links from the extracted url.
"""
from lib import wiki_get_links
import random
import datetime


random.seed(datetime.datetime.now())


def main():
    links = wiki_get_links('/wiki/donut')
    try:
        while len(links) > 0:
            new_article = random.choice(links).attrs['href']
            print(new_article)
            links = wiki_get_links(new_article)
    except TypeError as e:
        return None


if __name__ == '__main__':
    main()
