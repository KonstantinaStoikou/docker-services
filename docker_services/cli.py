# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Docker-Services is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""CLI module."""

import click
import site

from pathlib import Path

from .env import export_env_vars
from .services import services_down, services_up, all_services_up


def _services_filepath():
    """Calculates the services file path based on the current site-packages."""
    sites = site.getsitepackages()

    for _site in sites:
        path = Path(f"{_site}/docker_services/docker-services.yml")
        if path.exists() and path.is_file():
            return str(path)


@click.group()
@click.version_option()
def cli():
    """Initialize CLI context."""


@cli.command()
@click.argument(
    "action",
    default="up",
    required=False,
    type=click.Choice(["up", "down"], case_sensitive=False),
)
@click.argument("services", nargs=-1, required=False)  # -1 incompat with default
@click.option(
    "--filepath", "-f", required=False, help="Path to a custom docker compose file.",
)
def services(action, services, filepath):
    """Boots up or down the required services."""
    services = list(services)  # tuple to list
    export_env_vars()
    filepath = filepath if filepath else _services_filepath()
    if action == "up":
        services_up(services, filepath)

    else:
        services_down(filepath)


@cli.command()
@click.argument("services", nargs=-1, required=False)  # -1 incompat with default
@click.option(
    "--filepath", "-f", required=False, help="Path to a custom docker compose file.",
)
def wait_all_services_up(services, filepath):
    """Wait until all the containers for all the given services are up."""

    filepath = filepath if filepath else _services_filepath()
    all_up = all_services_up(services, filepath)
    while not all_up:
        all_up = all_services_up(services, filepath)

    click.secho("All services are up.")

