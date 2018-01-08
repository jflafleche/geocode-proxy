Command Line Interface Usage
============================
This is the reference for the command line interface of `geocode-proxy`.

CLI Usage Examples
------------------
The CLI can be used to query addresses using a specific service provider:

.. code-block:: bash
    :caption: CLI with specific service provider

    $ python3 cli.py "CN Tower" --service Google
    {'lat': 43.6425662, 'lng': -79.3870568}


If the service argument is omitted, `geocode-proxy` will 
make use of all available service providers to provide fallbacks 
if the primary service provider is unavailable:

.. code-block:: bash
    :caption: CLI with fallbacks

    $ python3 cli.py "CN Tower"
    {'lat': 43.6425662, 'lng': -79.3870568}