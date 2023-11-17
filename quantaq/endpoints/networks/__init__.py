from quantaq.endpoints import Domain


class Networks(Domain):
    """
    Note: the Networks endpoint is scoped within the Orgs endpoint,
    so all requests for networks (all or singular) are in the context
    of a particular organization.    
    """

    def list(self, **kwargs):
        """
        Return a list of networks accessible by the account,
        in the context of the org with id=org_id.

        :param int org_id: The parent org id.
        :param str limit: Limit the number of results returned
        :param str sort: Sort the results by a specific attribute
        :param str filter: Filter the query
        :param int per_page: Define the number of results to return per page

        :returns: Networks
        :rtype: list of dict
        """
        org_id = kwargs.pop("org_id")
        return self.client.requests(f"orgs/{org_id}/networks/", **kwargs)
    
    def get(self, **kwargs):
        """
        Return network with id=network_id in org with id=org_id.

        :param int org_id: The parent org id
        :param int network_id: The network id

        :returns: Network information
        :rtype: dict
        """
        org_id = kwargs.pop("org_id")
        network_id = kwargs.pop("network_id")
        
        return self.client.requests(f"orgs/{org_id}/networks/{network_id}", **kwargs)
