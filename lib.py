import requests
from requests.exceptions import HTTPError, ConnectionError
from bs4 import BeautifulSoup
import re


def getTitle(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError as e:     # Page not exist
        return None
    except ConnectionError:    # bad url, or no internet connection
        return None
    except Exception:
        print('Something went wrong!')
        return None

    try:
        bs = BeautifulSoup(r.text, 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    except Exception:
        print('Something went wrong!')
    return title


def wiki_get_links(article_url):
    """It finds all the article urls inside a wiki article page."""
    try:
        r = requests.get('http://en.wikipedia.org{}'.format(article_url))
        r.raise_for_status()
    except HTTPError:
        print('The page does not exist!')
        return None
    except ConnectionError:
        print('Bad link, or check your internet connection!')
        return None

    try:
        bs = BeautifulSoup(r.text, 'html.parser')
        articles = bs.find('div', {'id': 'bodyContent'}).find_all(
            'a', {'href': re.compile('^(/wiki/)((?!:).)*$')}
        )
        return articles
    except AttributeError:
        print('Cannot find the content!')
        return None
    except Exception:
        print('Something went wrong!')
        return None
