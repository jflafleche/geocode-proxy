Getting Started
===============

The following describes how to install geocode-proxy from GitHub.

GitHub Install
--------------
.. code-block:: bash

    $ git clone https://github.com/TODO
    $ cd geocode-proxy
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    $ pip3 install -r requirements.txt

Setting Up Credentials (Optional)
---------------------------------
The configuration file `config.json` is used to hold the provider 
keys for Google, Here and Bing providers. 

*Note: Without this step, geocode-proxy will rely only on the  
Google service and will not benefit from robustness of having 
access to multiple providers. In addition, the frequency of geocode 
requests will be restricted.*

.. code-block:: bash

    $ touch config.json

Example Configuration File
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript
    :caption: config.json

    {
        "Google": {
            "API_KEY": <insert Google api_key here>
        },
        "Here": {
            "APP_ID": <insert Here app_id here>,
            "APP_CODE": <insert Here app_code here>
        },
        "Bing": {
            "KEY": <insert Bing key here>
        }
    }