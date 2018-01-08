# coding: utf8

import sys
import os
import json

from providers.google import get_google_geocode
from providers.here import get_here_geocode
from providers.bing import get_bing_geocode


class Providers(object):
    SERVICES = {
        'Google': get_google_geocode,
        'Here': get_here_geocode,
        'Bing': get_bing_geocode,
    }
    CONFIG_PATH = './config.json'

    def __init__(self):
        self.CREDENTIALS = {}
        self._load_config()

    def _load_config(self):
        if os.path.isfile(self.CONFIG_PATH):
            with open(self.CONFIG_PATH) as config_file:
                self.CREDENTIALS = json.load(config_file)

    def get(self, provider, address):
        params = {'address': address}
        if provider in self.CREDENTIALS:
            params['credentials'] = self.CREDENTIALS[provider]
        
        return self.SERVICES[provider](**params)

    def get_with_fallback(self, address):
        for provider in self.SERVICES:
            provider_response = self.get(provider, address)
            if provider_response.status != 'No Key Provided':
                response = provider_response

            if response.is_success:
                break

        return response
