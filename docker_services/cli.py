# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Docker-Services is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""CLI module."""

import click

from .services import services_down, services_up

@click.group()
@click.version_option()
def cli():
    """Initialize CLI context."""

@cli.command()
@click.argument('action', default='up', required=False,
                type=click.Choice(['up', 'down'], case_sensitive=False))
@click.argument('services', nargs=-1, required=True)  # -1 incompat with default
def services(action, services):
    """Boots up or down the required services."""
    services = list(services)  # tuple to list
    if action == 'up':
        services_up(services)

    else:
        services_down(services)
