#!/usr/bin/python
# coding: utf8

from flask import Flask, request, abort, make_response, jsonify

from providers import Providers


app = Flask(__name__)

providers = Providers()

def get_latlng_by_address(address):
    response = providers.get_with_fallback(address)
    if response.is_success:
        return jsonify(response.data)
    elif response.status == 'No Results':
        abort(404, 'No results found')
    else:
        abort(502, 'None of the service providers could be reached.')

@app.route('/<address>', methods=['GET'])
def get_latlng(address):
    if not address:
        abort(400, 'Please provide an address.')

    return get_latlng_by_address(address)

@app.route('/', methods=['POST'])
def post_latlng():
    if not (request.json and request.json.get('address')):
        abort(400, 'Please provide an address.')

    return get_latlng_by_address(request.json['address'])

@app.errorhandler(404)
@app.errorhandler(400)
@app.errorhandler(502)
def not_found(error):
    return make_response(jsonify({'error': error.description}), error.code)


if __name__ == '__main__':
    app.run(debug=True)
