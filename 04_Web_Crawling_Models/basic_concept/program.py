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


def scrape_Brookings(url):
    bs = get_page(url)
    title = bs.find('h1').text
    body = bs.find('div', {'class': 'post-body post-body-enhanced'}).text
    return Content(url, title, body)


def scrape_NYTimes(url):
    bs = get_page(url)
    title = bs.find('h1').text
    paragraphs = bs.find_all('p', {"class": "css-n7ezar e2kc3sl0"})
    body = '\n'.join([paragraph.text for paragraph in paragraphs])
    return Content(url, title, body)


url_NYTimes = ('https://www.nytimes.com/2018/05/07/nyregion/'
               'new-york-attorney-general-eric-schneiderman-abuse.html')
url_Brookings = ('https://www.brookings.edu/blog/future-development/2018/'
                 '05/04/a-leap-in-gender-equality-begins-with-better-data/')
content_NYTimes = scrape_NYTimes(url_NYTimes)
content_Brookings = scrape_Brookings(url_Brookings)

print('Title: {}'.format(content_Brookings.title))
print('URL: {}\n'.format(content_Brookings.url))
print(content_Brookings.body)
