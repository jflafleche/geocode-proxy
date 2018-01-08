# coding: utf8

from __future__ import absolute_import
import json

try:
    from urllib2 import urlopen
    from urllib2 import URLError
    from urllib import urlencode
except ImportError:
    from urllib.request import urlopen
    from urllib.error import URLError
    from urllib.parse import urlencode

from providers.location_response import LocationResponse


def get_bing_geocode(address, credentials=None):
    URL = 'http://dev.virtualearth.net/REST/v1/Locations'
    
    req_params = {
        'q': address,
        'maxResults': 1,
    }

    if credentials and 'KEY' in credentials:
        req_params['key'] = credentials['KEY']
    else:
        return LocationResponse(status='No Key Provided')

    req = URL + '?' + urlencode(req_params)

    try:
        resp = urlopen(req)
        response_dict = json.loads((resp.read().decode('utf-8')))
    except URLError as e:
        return LocationResponse(status=e.reason)

    return parse_response(response_dict)

def parse_response(response_dict):
    resources = response_dict['resourceSets'][0]['resources']

    if resources and resources[0]['confidence'] != 'Low':
        lat_lng = resources[0]['point']['coordinates']
        lat, lng = lat_lng[0], lat_lng[1]
        return LocationResponse('OK', lat, lng)
    else:
        return LocationResponse(status='No Results')
