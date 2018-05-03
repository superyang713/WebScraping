import requests
from requests.exceptions import HTTPError, ConnectionError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError as e:     # Page not exist
        return None
    except ConnectionError:    # bad url
        return None

    try:
        bs = BeautifulSoup(r.text, 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title
