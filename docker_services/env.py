# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Docker-Services is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Environment module."""

import os


def _setdefault_env(variable, default_value):
    """Set environmental variable value if it does not exist."""
    os.environ[variable] = os.environ.get(variable, default_value)


def export_env_vars():
    """ Export the environment variables for services and versions."""
    # export variables for latest versions
    _setdefault_env("ES_5_LATEST", "5.6.10")
    _setdefault_env("ES_6_LATEST", "6.8.12")

    _setdefault_env("ES_7_LATEST", "7.9.0")
    _setdefault_env("POSTGRESQL_9_LATEST", "9.6.19")
    _setdefault_env("POSTGRESQL_10_LATEST", "10.14")
    _setdefault_env("POSTGRESQL_11_LATEST", "11.9")
    _setdefault_env("MYSQL_5_LATEST", "5.7.31")
    _setdefault_env("MYSQL_8_LATEST", "8.0.21")
    _setdefault_env("REDIS_6_LATEST", "6.0.6")
    _setdefault_env("MEMCACHED_LATEST", "1.6.6")
    _setdefault_env("RABBITMQ_3_LATEST", "3.8.7")

    # export default services
    _setdefault_env("DB", "postgresql")
    _setdefault_env("ES", "es")
    _setdefault_env("CACHE", "redis")

    # Elasticsearch
    _setdefault_env("ES_VERSION", "7.2.0")

    # PostrgreSQL
    _setdefault_env("POSTGRESQL_VERSION", "9.6")
    _setdefault_env("POSTGRESQL_USER", "invenio")
    _setdefault_env("POSTGRESQL_PASSWORD", "invenio")
    _setdefault_env("POSTGRESQL_DB", "invenio")

    # MySQL
    _setdefault_env("MYSQL_USER", "invenio")
    _setdefault_env("MYSQL_PASSWORD", "invenio")
    _setdefault_env("MYSQL_DB", "invenio")
    _setdefault_env("MYSQL_ROOT_PASSWORD", "invenio")
