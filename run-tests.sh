#!/usr/bin/env sh
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Docker-Services is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

pydocstyle docker_services tests docs && \
isort docker_services tests --check-only --diff && \
check-manifest --ignore ".travis-*" && \
sphinx-build -qnNW docs docs/_build/html && \
pytest
