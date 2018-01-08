#!/usr/bin/env python
# coding: utf8
from __future__ import absolute_import
import click

from providers import Providers


providers = Providers()

@click.command()
@click.argument('address')
@click.option('--service', '-s', type=click.Choice(providers.SERVICES))
def cli(address, service=None):
    if service:
        response = providers.get(service, address)
    else:
        response = providers.get_with_fallback(address)

    print(gen_output(response))

def gen_output(response):
    if response.is_success:
        return response.data
    
    if response.status == 'Bad Request':
        return 'Error: Invalid address.'
    elif response.status == 'No Results':
        return 'Error: No results found.'
    elif response.status == 'Not Found':
        return 'Error: None of the service providers could be reached.'
    else:
        return 'Error: ' + response.status


if __name__ == "__main__":
    cli()
