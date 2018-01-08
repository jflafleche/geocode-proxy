# geocode-proxy
A simple-to-use service that returns the latitude and longitude the 
the most relevant point to a provided address. This service implements 
multiple service providers in order to provide robust capabilities in 
the event that the main provider is unavailable.

Geocode-Proxy currently supports `Google`, `Bing` and `Here` geocode services.

Documentation: [geocode-proxy.readthedocs.org](http://geocode-proxy.readthedocs.org)

## Getting Started
The following describes how to install geocode-proxy from GitHub.

### GitHub Install
```bash
$ git clone https://github.com/jflafleche/geocode-proxy
$ cd geocode-proxy
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```
### Setting Up Credentials (Optional)
The configuration file `config.json` is used to hold the provider 
keys for Google, Here and Bing providers. 

*Note: Without this step, geocode-proxy will rely only on the  
Google service and will not benefit from robustness of having 
access to multiple providers. In addition, the frequency of geocode 
requests will be restricted.*

To create the configuration file:
```bash
$ touch config.json
```

#### Example Configuration File

```json
{
    "Google": {
        "API_KEY": "<insert Google api_key here>"
    },
    "Here": {
        "APP_ID": "<insert Here app_id here>",
        "APP_CODE": "<insert Here app_code here>"
    },
    "Bing": {
        "KEY": "<insert Bing key here>"
    }
}
```

## Documentation
Please visit [geocode-proxy.readthedocs.org](http://geocode-proxy.readthedocs.org) 
for further details.