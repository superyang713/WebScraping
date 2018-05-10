class Content:
    """
    Common base class for all articles/pages
    """
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Flexible printing function controls output
        """
        print('TITLE: {}'.format(self.title))
        print('BODY:\n{}'.format(self.body))
        print('URL: {}'.format(self.url))
        print('-' * 30)
