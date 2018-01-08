# coding: utf8

import json
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError

from providers.location_response import LocationResponse


def get_here_geocode(address, credentials=None):
    URL = 'https://geocoder.cit.api.here.com/6.2/geocode.json'
    
    if credentials and 'APP_ID' in credentials and 'APP_CODE' in credentials:
        req_params = {
            'app_id': credentials['APP_ID'],
            'app_code': credentials['APP_CODE'],
            'searchtext': address,
        }
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
    views = response_dict['Response']['View']
    if views:
        lat_lng = views[0]['Result'][0]['Location']['DisplayPosition']
        lat, lng = lat_lng['Latitude'], lat_lng['Longitude']
        return LocationResponse('OK', lat, lng)
    else:
        return LocationResponse(status='No Results')