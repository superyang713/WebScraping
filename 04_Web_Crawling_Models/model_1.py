import requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body


def get_page(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser')


def scrape_NYTimes(url):
    bs = get_page(url)
    title = bs.find('h1').text
    paragraphs = bs.find_all('p', {'class': 'story-content'})
    body = '\n'.join([paragraph.text for paragraph in paragraphs])
    return Content(url, title, body)


def scrape_Brookings(url):
    bs = get_page(url)
    title = bs.find('h1').text
    paragraphs = bs.find_all('p', {"class": "css-n7ezar e2kc3sl0"})
    body = '\n'.join([paragraph.text for paragraph in paragraphs])
    return Content(url, title, body)


url_NYTimes = ('https://www.nytimes.com/2018/05/07/nyregion/'
               'new-york-attorney-general-eric-schneiderman-abuse.html')
content = scrape_NYTimes(url_NYTimes)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)
