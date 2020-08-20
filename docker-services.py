import os

from env import export_env_vars

export_env_vars()

# FIXME: be able to override env vars from command line before running docker-compose

os.system("docker-compose up -d")
os.system("docker-compose down")

