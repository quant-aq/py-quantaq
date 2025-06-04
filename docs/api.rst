.. currentmodule:: quantaq

API Reference
=============

Clients
-------

.. rubric:: API Client

API clients form the basis for making API requests. Typically, you will use the QuantAQAPIClient 
which will connect you directly to the QuantAQ website. If using an enterprise version of 
the QuantAQ API and server, you can build your own API client following the instructions in the 
Usage section.

.. autosummary::
    :toctree: generated/

    client.ClientBase
    client.APIClient
    client.DevelopmentAPIClient
    client.StagingAPIClient
    client.ProductionAPIClient
    QuantAQAPIClient

API Endpoints
-------------

The following is an extensive list of all available API endpoints. Please check 
the Usage section for instructions on how to use them.

.. rubric:: Users Endpoints

.. autosummary::
    :toctree: generated/

    endpoints.users.Users.list
    endpoints.users.Users.get
    endpoints.users.Users.update


.. rubric:: Organizations Endpoints

.. autosummary::
    :toctree: generated/

    endpoints.organizations.Organizations.list
    endpoints.organizations.Organizations.get


.. rubric:: Networks Endpoints

.. autosummary::
    :toctree: generated/

    endpoints.networks.Networks.list
    endpoints.networks.Networks.get


.. rubric:: Devices Endpoints

.. autosummary::
    :toctree: generated/

    endpoints.devices.Devices.list
    endpoints.devices.Devices.get
    endpoints.devices.Devices.update
    endpoints.devices.Devices.add
    endpoints.devices.Devices.drop


.. rubric:: Data Endpoints

.. autosummary::
    :toctree: generated/

    endpoints.data.Data.list
    endpoints.data.Data.bydate
    endpoints.data.Data.get

.. rubric:: Solar Power System Data Endpoints
    
.. autosummary::
    :toctree: generated/

    endpoints.solar.Solar.list


.. rubric:: Logs Endpoints

.. autosummary::
    :toctree: generated/

    endpoints.logs.Logs.list
    endpoints.logs.Logs.get
    endpoints.logs.Logs.update
    endpoints.logs.Logs.drop


.. rubric:: Cellular Logs Endpoints

.. autosummary::
    :toctree: generated/

    endpoints.cellular.Cellular.list
    endpoints.cellular.Cellular.drop


.. rubric:: Models Endpoints

.. autosummary::
    :toctree: generated/

    endpoints.models.Models.add
    endpoints.models.Models.get


Utilities
---------

.. rubric:: Utils

.. autosummary::
    :toctree: generated/

    utils.to_dataframe