API Reference
=============
The `geocode-proxy` service exposes `GET` and `POST` endpoints 
to retrieve *latitude* and *longitude* of a requested address string. 
Both `GET` and `POST` return the most relevant result in JSON format.

Response
--------
The service response is a JSON object with latitude and longitude.

Usage Example
--------------
Setting up a local server:

.. code-block:: bash
    :caption: local server

    $ python3 app.py

Now we can request the latitude and longitude with a `GET` request:

.. code-block:: bash
    :caption: GET

    $ curl http://127.0.0.1:5000/CN+TOWER
    {
        "lat": 43.6425662, 
        "lng": -79.3870568
    }

or with a `POST` request:

.. code-block:: bash
    :caption: POST

    $ curl -i -H "Content-Type: application/json" -X POST -d '{"address":"CN Tower"}' http://127.0.0.1:5000/
    {
        "lat": 43.6425662, 
        "lng": -79.3870568
    }

Error Handling
--------------
If no address is provided, if no result is found by any of the providers, 
or if no response is obtained from any of the available providers, 
the service will return an HTTP error code along with a JSON output of 
the error.

.. code-block:: bash
    :caption: No Address Provided

    $ curl -i -H "Content-Type: application/json" -X POST -d '{"address":""}' http://127.0.0.1:5000/
    HTTP/1.0 400 BAD REQUEST
    Content-Type: application/json
    Content-Length: 44
    Server: Werkzeug/0.12.2 Python/3.6.3
    Date: Mon, 08 Jan 2018 00:44:25 GMT

    {
        "error": "Please provide an address."
    }

.. code-block:: bash
    :caption: Not Found

    $ curl -i http://127.0.0.1:5000/The+Wardrobe+Narnia
    HTTP 1.0, assume close after body
    HTTP/1.0 404 NOT FOUND
    Content-Type: application/json
    Content-Length: 34
    Server: Werkzeug/0.12.2 Python/3.6.3
    Date: Mon, 08 Jan 2018 00:40:07 GMT
     
    {
        "error": "No results found"
    }

.. code-block:: bash
    :caption: Could Not Reach Providers

    $ curl -i http://127.0.0.1:5000/CN+Tower
    HTTP 1.0, assume close after body
    HTTP/1.0 502 BAD GATEWAY
    Content-Type: application/json
    Content-Length: 65
    Server: Werkzeug/0.12.2 Python/3.6.3
    Date: Mon, 08 Jan 2018 00:42:31 GMT
     
    {
        "error": "None of the service providers could be reached."
    }


