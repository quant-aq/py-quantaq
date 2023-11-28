.. highlight:: sh

Using this Library
==================

Credentials
-----------

To use the QuantAQ API, you must have an API token. This can be obtained 
only via the website when logged in to your account. This token should 
be stored as an environment variable called **QUANTAQ_APIKEY** in order 
to be automagically be discovered. You can also set it when you intiate 
a client as seen below.


Setup and Authentication
-------------------------

There are several clients that can be used, with :class:`quantaq.QuantAQAPIClient` 
being your best bet. You can also create your own from :class:`quantaq.client.APIClient` if 
you are using an enterprise server at a different domain.

To initiate the client (assuming you have set your API key as an environment variable):

.. code-block:: python

    >>> import quantaq
    >>> client = quantaq.QuantAQAPIClient()


If you would like to set your API key at initialization:

.. code-block:: python

    >>> client = quantaq.QuantAQAPIClient(api_key="***")


If you did not properly set the API key, an exception will be raised.


Customize the Client
^^^^^^^^^^^^^^^^^^^^

If you would like to customize the client to use a custom 
domain or API version, you can do so by creating a new class:

.. code-block:: python 

    from quantaq.client import APIClient

    class CustomAPIClient(APIClient):
        def __init__(self, api_key=None):
            super().__init__("https://custom.domain/api", version="v1", api_key=api_key)


You can then use it just as you would the :class:`quantaq.QuantAQAPIClient` class:

.. code-block:: python

    >>> client = CustomAPIClient()


Account Information
--------------------

The API client offers easy access to all available QuantAQ API endpoints. To 
obtain your user account information, you can use the `whoami` method:

.. code-block:: python

    >>> whoami = client.whoami()
    >>> print (whoami)


Organizations
-------------

List All Organizations
^^^^^^^^^^^^^^^^^^^^^^

You can retrieve a list of all the organizations visible to you:

.. code-block:: python

    >>> organizations = client.organizations.list()
    >>> print (organizations)

Get a Single Organization
^^^^^^^^^^^^^^^^^^^^^^^^^

To get information about a specific organization, you can use the `get` method 
with the id as an argument:

.. code-block:: python

    >>> organization = client.organizations.get(id=1)
    >>> print (organization)


Networks
--------

List All Networks
^^^^^^^^^^^^^^^^^

You can retrieve a list of all the networks visible to you, in the context of 
a given organization, with the organization_id as an argument:

.. code-block:: python

    >>> networks = client.networks.list(organization_id=1)
    >>> print (networks)

Get a Single Network
^^^^^^^^^^^^^^^^^^^^

To get information about a specific network, you can use the `get` method 
with the parent organization_id and the network_id as arguments:

.. code-block:: python

    >>> network = client.networks.get(organization_id=1, network_id=1)
    >>> print (network)


Devices
--------

List All Devices
^^^^^^^^^^^^^^^^

To get a list of all devices:

.. code-block:: python

    >>> devices = client.devices.list()
    >>> print (devices)

Get a Single Device
^^^^^^^^^^^^^^^^^^^

You can also use the :meth:`quantaq.utils.to_dataframe` utility 
function to convert the list to a dataframe:

.. code-block:: python

    >>> from quantaq.utils import to_dataframe
    >>> devices = to_dataframe(client.devices.list())
    >>> print (devices)

Devices - Advanced Queries
^^^^^^^^^^^^^^^^^^^^^^^^^^

Devices are filterable by organization and network, using the organization_id and network_id
kwargs. For example, to get the devices in a particular organization:

.. code-block:: python

    >>> devices = client.devices.list(organization_id=1)
    >>> print (devices)


You can also limit the number of devices to return using the `limit` kwarg or 
apply advanced filters using the `filter` kwarg. More details on how to 
generate advanced queries can be found in the **Advanced Queries** section 
near the bottom of this document. However, here are a few examples:

Return only the first ten devices:

.. code-block:: python

    >>> devices = client.devices.list(limit=10)
    >>> print (devices)


Return only devices with **device_state=ACTIVE**:

.. code-block:: python

    >>> devices = client.devices.list(filter="device_state,eq,ACTIVE")
    >>> print (devices)


Data
----

Data on the QuantAQ platform is described as either **final** 
data (e.g. PM1, PM2.5, CO, etc) which is cleaned, QA/QC'd, and 
ready to analyze, as well as **raw** data (e.g., voltages, raw bin 
counts for particle counters) which is only available to researchers and 
devices that you are allowed to view. If you have more questions about 
who can see what data, please feel free to reach out to us.

List All Final Data for a Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can only retrieve data for a specific device and must reference 
it by its serial number (`sn`). For example, we can retrieve the data 
between two dates:

.. code-block:: python

    >>> from quantaq.utils import to_dataframe
    >>> data = client.data.list(sn="SN000-000", start="2020-01-01 00:00", stop="2020-01-01 03:30")
    >>> data = to_dataframe(data)
    >>> print (data)


While you don't necessarily have to define either a start or stop point, it is highly
recommended. If you don't, the response can take some time as it is iterating through 
a large number of API requests to retrieve the paginated results.

.. tip::

   It is best to use this endpoint for querying less than one day of data. If trying to return 
   large chunks of data, use the `bydate` function detailed below.


List All Raw Data for a Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you would like to retrieve the raw data, you need to specify that 
in your request:

.. code-block:: python

    >>> data = client.data.list(sn="SN000-000", start="2020-01-01", stop="2020-01-03", raw=True)
    >>> print (data)


Retrieve Large Chunks of Data for a Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. attention::

    This endpoint was added with release 1.1.0 on March 31st, 2022.


To retrieve large chunks of data, it is best to use the `bydate` function.

.. code-block:: python

    >>> data = client.data.bydate(sn='SN000-000', date='2022-01-01')
    >>> data = to_dataframe(data)
    >>> print (data)

This will retrieve all available all available data for a given device on a given date. To 
get data for many dates, simply iterate over all of the dates:

.. code-block:: python

    >>> import pandas as pd
    >>> df = []
    >>> for each in pd.date_range(start='2022-01-01', end='2022-01-15'):
    >>>     df.append(
    >>>         to_dataframe(client.data.bydate(sn='SN000-000', date=str(each.date())))
    >>>     )
    >>> df = pd.concat(df)
    >>> print (df.info())



Limit Your Data Requests
^^^^^^^^^^^^^^^^^^^^^^^^

You can also limit your data requests so that you only return a 
limited number of data points:

.. code-block:: python

    >>> data = client.data.list(sn="SN000-000", start="2020-01-01", limit=100)
    >>> print (data)


Return the Most Recent Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can combine filtering and limit to return just the most 
recent data point:

.. code-block:: python

    >>> recent = client.data.list(sn="SN000-000", sort="timestamp,asc", limit=1)
    >>> print (recent)

However, this is the default behaviour, so it is generally not necessary to add the 
sort. If you just return one data point, it will by default be the most recent.


Advanced Data Requests
^^^^^^^^^^^^^^^^^^^^^^

You can also return just data that meets specific criteria. For example,
 if we want to return just data where carbon monoxide is between 200-1000 ppb:

.. code-block:: python

    >>> data = client.data.list(sn="SN000-000", start="2020-01-01", filter="co,ge,200;co,le,1000")
    >>> print (data)

Logs
----

List All Logs for a Device
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can list all logs for a specific device using:

.. code-block:: python

    >>> logs = client.logs.list(sn="SN000-000", limit=100)
    >>> print (logs)

Like the data endpoint above, you can use the **start** and **stop** 
arguments to limit which logs to obtain.

Get a Single Log
^^^^^^^^^^^^^^^^

You can obtain a single log by referencing its ID, which can 
be obtained from the list of logs above:

.. code-block:: python

    >>> log = client.logs.get(id=111)
    >>> print (log)

Update a Log
^^^^^^^^^^^^

You can update a log (if you have permissions to do so) by using 
the **update** method:

.. code-block:: python

    >>> log = client.logs.update(id=111, message="<custom message here>", level="INFO")
    >>> print (log)

Drop a Log
^^^^^^^^^^

You can also drop/delete a log if you have permissions:

.. code-block:: python

    >>> result = client.logs.drop(id=111)
    >>> print (result)


Cellular Logs
-------------

Cellular logs are custom logs that contain detailed information about 
the state of the cellular or wireless connection of your devices.

List All Cellular Logs
^^^^^^^^^^^^^^^^^^^^^^

You can list all cellular logs:

.. code-block:: python

    >>> cell = client.cellular.list(sn="SN000-000", limit=100)
    >>> print (cell)

Drop a Cellular Log
^^^^^^^^^^^^^^^^^^^

You can also drop/delete a cellular log (if you have permissions):

.. code-block:: python

    >>> result = client.cellular.drop(id=1)
    >>> print (result)

Models (ML Models)
------------------

Models summarize the machine learning models used to convert raw 
voltages and particle bin counts to the final data. While the model 
itself is not available, the summary statistics, error metrics, and 
a summary of the model can be retrieved.

Get the Models for a Single Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To get the models used by a specific device:

.. code-block:: python

    >>> models = client.models.list(sn="SN000-000")
    >>> print (models)


Advanced Queries
----------------

The API itself has quite powerful querying capabilities that can be separated into 
three categories: filtering, limiting, and sorting responses. Below are a brief overview 
of each.

Limiting Responses
^^^^^^^^^^^^^^^^^^

To limit the number of results that are returned for the endpoints that return many 
items, you can use the **limit** keyword argument. The only requirement is that it must 
be an integer (e.g., **limit=5**). 

As an example, if we want to return just the first 5 devices, we can add the limit keyword 
argument as follows:

.. code-block:: python

    >>> devices = client.devices.list(limit=5)
    >>> print (len(devices))

Sorting Responses
^^^^^^^^^^^^^^^^^

You can sort the results returned using the **sort** keyword argument. To use, you must provide both 
a column to sort by as well as a sort instruction (either **asc** or **desc**). The final format 
looks like **sort=[column],[asc or desc]**. You can also join multiple sorts together using a semicolon.

As an example, if we want to sort the list of devices by their serial number:

.. code-block:: python

    >>> devices = client.devices.list(sort="sn,asc")


This can be quite useful when combined with the limit function! For example, if we want to return the 
100 highest CO values:

.. code-block:: python

    >>> data = client.data.list(sn="SN000-000", sort="co,asc", limit=100)
    >>> print (data)


Filtering
^^^^^^^^^

Filtering allows us to build incredibly detailed queries. There are several arguments that 
can be used to build queries including:

  * `eq`: equals
  * `ne`: not equals
  * `lt`: less than
  * `le`: less than or equal to
  * `gt`: greater than
  * `ge`: greater than or equal to
  * `in`: in
  * `like`: like

The format of the argument must be `filter="[column],[arg],[value]"`. Like with sort, 
you can combine many filters together using a semicolon.

For example, if we want to get all data where CO > 1000 ppb:

.. code-block:: python

    >>> data = client.data.list(sn="SN000-000", filter="co,gt,1000")
    >>> print (data)


If we want to grab the first 100 points where 1000 <= CO <= 5000 ppb:

.. code-block:: python

    >>> data = client.data.list(sn="SN000-000", filter="co,ge,1000;co,le,5000", limit=100)
    >>> print (data)


If you have more questions about how to build queries, feel free to add an issue to the 
GitHub repository.