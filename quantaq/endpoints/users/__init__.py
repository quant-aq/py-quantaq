import json
from quantaq.endpoints import (
    Domain, 
    GET, PUT, POST, DELETE
)

class Users(Domain):
    """Initialize the Users group of endpoints.

    :returns: Domain for Users
    :rtype: quantaq.models.Users
    """
    def __init__(self, client) -> None:
        super(Users, self).__init__(client)

    def list(self, **kwargs):
        """Return all (available) users.

        :param str limit: Limit the number of results returned
        :param str sort: Sort the results by a specific attribute
        :param str filter: Filter the query
        :param int per_page: Define the number of results to return per page

        :returns: List of users.
        :rtype: list of dict
        """
        return self.client.requests("users/", **kwargs)

    def get(self, **kwargs):
        """Return user with id = id.

        :param int id: The user id

        :returns: User information
        :rtype: dict
        """
        id = kwargs.pop("id")

        return self.client.requests("users/" + str(id))

    def update(self, **kwargs):
        """Update the record of a user with id = user_id

        All user parameters that are not listed here must be 
        changed via the UI.

        :param int id: The user id
        :param str first_name: First name of the user
        :param str last_name: Last name of the user

        :returns: User information
        :rtype: dict
        """
        id = kwargs.pop("id")
        
        return self.client.requests("users/" + str(id), verb=PUT, **kwargs)
