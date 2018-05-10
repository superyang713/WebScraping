"""
This is just a demostration that when crawling different types of
websites/webpages, it would be better to use subclasses.
"""

# If websites are similar, then use one class.
class Website:
    """
    Common base class for all articles/pages
    """
    def __init__(self, name, url, title_tag, body_tag):
        self.name = name
        self.url = url
        self.title_tag = title_tag
        self.body_tag = body_tag


# If websites are different, then use subclasses.
class Webpage:
    """
    Common base class for all articles/pages
    """
    def __init__(self, name, url, title_tag):
        self.name = name
        self.url = url
        self.title_tag = title_tag


class Product(Webpage):
    """
    Contains information for scraping a product page.
    """
    def __init__(self, name, url, title_tag, product_number, price_tag):
        super().__init__(name, url, title_tag)
        self.product_number = product_number
        self.price_tag = price_tag


class Article(Webpage):
    """
    Contains information for scraping a article page.
    """
    def __init__(self, name, url, title_tag, body_tag, date_tag):
        super().__init__(self, name, url, title_tag)
        self.body_tag = body_tag
        self.date_tag = date_tag
