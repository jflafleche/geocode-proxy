# coding: utf8

class LocationResponse(object):
    def __init__(self, status='', lat=None, lng=None):
        self.status = status
        self.lat = lat
        self.lng = lng
    
    @property
    def data(self):
        return {'lat': self.lat, 'lng': self.lng}

    @property
    def is_success(self):
        return self.status == 'OK'
