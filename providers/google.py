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


def get_google_geocode(address, credentials=None):
    URL = 'https://maps.googleapis.com/maps/api/geocode/json'

    req_params = {'address': address}
    if credentials and 'API_KEY' in credentials:
        req_params['key'] = credentials['API_KEY']

    req = URL + '?' + urlencode(req_params)
    try:
        resp = urlopen(req)
        response_dict = json.loads((resp.read().decode('utf-8')))
    except URLError as e:
        return LocationResponse(status=e.reason)

    return parse_response(response_dict)

def parse_response(response_dict):
    results = response_dict['results']
    if results:
        lat_lng = results[0]['geometry']['location']
        lat, lng = lat_lng['lat'], lat_lng['lng']
        return LocationResponse('OK', lat, lng)
    else:
        return LocationResponse(status='No Results')
