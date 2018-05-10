class Website:
    """
    Contains information about website structure
    """
    def __init__(self, name, url, search_url, result_listing, result_url,
                 absolute_url, title_tag, body_tag):
        self.name = name
        self.url = url
        self.search_url = search_url
        self.result_listing = result_listing
        self.result_url = result_url
        self.absolute_url = absolute_url
        self.title_tag = title_tag
        self.body_tag = body_tag
