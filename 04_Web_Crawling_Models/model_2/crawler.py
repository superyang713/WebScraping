from content import Content
import requests
from bs4 import BeautifulSoup


class Crawler:
    """
    A crawler that scrape title and body content from a website.
    """
    def get_page(self, url):
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(r.text, 'html.parser')

    def safe_get(self, page_obj, selector):
        """
        Untility function used to get a content string from a BeautifulSoup
        object and a selector. Returns an empty string if no object is found
        for the given selector
        """
        selected_elements = page_obj.select(selector)
        if selected_elements is not None and len(selected_elements) > 0:
            return '\n'.join(
                [elem.get_text() for elem in selected_elements])
        return ''

    def parse(self, site, url):
        """
        Extract content from a given page URL
        """
        bs = self.get_page(url)
        if bs is not None:
            title = self.safe_get(bs, site.titleTag)
            body = self.safe_get(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()
