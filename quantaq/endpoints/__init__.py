import json

GET = "GET"
PUT = "PUT"
DELETE = "DELETE"
POST = "POST"

class Domain(object):
    """
    This represents a single group of endpoints.
    """
    def __init__(self, client) -> None:
        """
        :param quantaq.client.ClientBase client: The API base client.
        """
        self.client = client