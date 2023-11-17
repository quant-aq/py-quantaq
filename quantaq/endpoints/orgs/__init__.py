from quantaq.endpoints import Domain


class Orgs(Domain):
    def list(self, **kwargs):
        """
        Return a list of orgs accessible by the account.

        :param str limit: Limit the number of results returned
        :param str sort: Sort the results by a specific attribute
        :param str filter: Filter the query
        :param int per_page: Define the number of results to return per page

        :returns: Orgs
        :rtype: list of dict
        """
        return self.client.requests("orgs/", **kwargs)
    
    def get(self, **kwargs):
        """
        Return org with id = id.

        :param int id: The org id

        :returns: Org information
        :rtype: dict
        """
        id = kwargs.pop("id")
        
        return self.client.requests("orgs/" + str(id))
