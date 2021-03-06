class MXStaticRoutes(object):
    def __init__(self, session):
        super(MXStaticRoutes, self).__init__()
        self._session = session
    
    def getNetworkStaticRoutes(self, networkId: str):
        """
        **List the static routes for an MX or teleworker network**
        https://api.meraki.com/api_docs#list-the-static-routes-for-an-mx-or-teleworker-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX static routes'],
            'operation': 'getNetworkStaticRoutes',
        }
        resource = f'/networks/{networkId}/staticRoutes'

        return self._session.get(metadata, resource)

    def createNetworkStaticRoute(self, networkId: str, name: str, subnet: str, gatewayIp: str):
        """
        **Add a static route for an MX or teleworker network**
        https://api.meraki.com/api_docs#add-a-static-route-for-an-mx-or-teleworker-network
        
        - networkId (string)
        - name (string): The name of the new static route
        - subnet (string): The subnet of the static route
        - gatewayIp (string): The gateway IP (next hop) of the static route
        """

        kwargs = locals()

        metadata = {
            'tags': ['MX static routes'],
            'operation': 'createNetworkStaticRoute',
        }
        resource = f'/networks/{networkId}/staticRoutes'

        body_params = ['name', 'subnet', 'gatewayIp']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkStaticRoute(self, networkId: str, staticRouteId: str):
        """
        **Return a static route for an MX or teleworker network**
        https://api.meraki.com/api_docs#return-a-static-route-for-an-mx-or-teleworker-network
        
        - networkId (string)
        - staticRouteId (string)
        """

        metadata = {
            'tags': ['MX static routes'],
            'operation': 'getNetworkStaticRoute',
        }
        resource = f'/networks/{networkId}/staticRoutes/{staticRouteId}'

        return self._session.get(metadata, resource)

    def updateNetworkStaticRoute(self, networkId: str, staticRouteId: str, **kwargs):
        """
        **Update a static route for an MX or teleworker network**
        https://api.meraki.com/api_docs#update-a-static-route-for-an-mx-or-teleworker-network
        
        - networkId (string)
        - staticRouteId (string)
        - name (string): The name of the static route
        - subnet (string): The subnet of the static route
        - gatewayIp (string): The gateway IP (next hop) of the static route
        - enabled (boolean): The enabled state of the static route
        - fixedIpAssignments (object): The DHCP fixed IP assignments on the static route. This should be an object that contains mappings from MAC addresses to objects that themselves each contain "ip" and "name" string fields. See the sample request/response for more details.
        - reservedIpRanges (array): The DHCP reserved IP ranges on the static route
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX static routes'],
            'operation': 'updateNetworkStaticRoute',
        }
        resource = f'/networks/{networkId}/staticRoutes/{staticRouteId}'

        body_params = ['name', 'subnet', 'gatewayIp', 'enabled', 'fixedIpAssignments', 'reservedIpRanges']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkStaticRoute(self, networkId: str, staticRouteId: str):
        """
        **Delete a static route from an MX or teleworker network**
        https://api.meraki.com/api_docs#delete-a-static-route-from-an-mx-or-teleworker-network
        
        - networkId (string)
        - staticRouteId (string)
        """

        metadata = {
            'tags': ['MX static routes'],
            'operation': 'deleteNetworkStaticRoute',
        }
        resource = f'/networks/{networkId}/staticRoutes/{staticRouteId}'

        return self._session.delete(metadata, resource)

