#!/usr/bin/env sh
# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Docker-Services is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

pydocstyle docker_services tests docs && \
isort docker_services tests --multi-line=3 --line-width=88 --trailing-comma --force-grid-wrap=0 --use-parentheses --check-only --diff && \
black --check --diff docker_services tests && \
check-manifest --ignore ".travis-*" && \
sphinx-build -qnNW docs docs/_build/html && \
pytest
