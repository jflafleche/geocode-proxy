#!/usr/bin/env python
# coding: utf8

import click
from providers import Providers

providers = Providers()

@click.command()
@click.argument('address')
@click.option('--service', '-s', type=click.Choice(providers.SERVICES))
def cli(address, service=None):
    if service:
        location_response = providers.get(service, address)
    else:
        location_response = providers.get_with_fallback(address)

    print(get_output(location_response))
    

def get_output(location_response):
    if location_response.is_success:
        return location_response.data
    else:
        return location_response.status

if __name__ == "__main__":
    cli()
