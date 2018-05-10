class Website:
    """
    Contains information about website structure
    """
    def __init__(self, name, url, target_pattern, absolute_url, title_tag,
                 body_tag):
        self.name = name
        self.url = url
        self.target_pattern = target_pattern
        self.absolute_url = absolute_url
        self.title_tag = title_tag
        self.body_tag = body_tag
