from quantaq.endpoints import Domain


class Organizations(Domain):
    def list(self, **kwargs):
        """
        Return a list of organizations accessible by the account.

        :param str limit: Limit the number of results returned
        :param str sort: Sort the results by a specific attribute
        :param str filter: Filter the query
        :param int per_page: Define the number of results to return per page

        :returns: Organizations
        :rtype: list of dict
        """
        return self.client.requests("orgs/", **kwargs)
    
    def get(self, **kwargs):
        """
        Return organizations with id = id.

        :param int id: The organization id

        :returns: Organizations information
        :rtype: dict
        """
        id = kwargs.pop("id")
        
        return self.client.requests("orgs/" + str(id))
