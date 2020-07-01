import json
from quantaq.endpoints import (
    Domain, 
    GET, PUT, POST, DELETE
)

class Teams(Domain):
    """
    """
    def __init__(self, client) -> None:
        super(Teams, self).__init__(client)
    
    def list(self, **kwargs):
        """Return a list of teams the account belongs to.

        :param str limit: Limit the number of results returned
        :param str sort: Sort the results by a specific attribute
        :param str filter: Filter the query
        :param int per_page: Define the number of results to return per page

        :returns: List of teams.
        :rtype: list of dict
        """
        return self.client.requests("teams/", **kwargs)
    
    def get(self, **kwargs):
        """Return team with id = id.

        :param int id: The team id

        :returns: Team information
        :rtype: dict
        """
        id = kwargs.pop("id")
        
        return self.client.requests("teams/" + str(id))