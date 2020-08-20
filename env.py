import os


def export_env_vars():
    """ Export the environment variables for services and versions."""
    # export variables for latest versions
    os.environ["ES_5_LATEST"] = "5.6.10"
    os.environ["ES_6_LATEST"] = "6.8.12"

    os.environ["ES_7_LATEST"] = "7.9.0"
    os.environ["PSQL_9_LATEST"] = "9.6.19"
    os.environ["PSQL_10_LATEST"] = "10.14"
    os.environ["PSQL_11_LATEST"] = "11.9"
    os.environ["MYSQL_5_LATEST"] = "5.7.31"
    os.environ["MYSQL_8_LATEST"] = "8.0.21"
    os.environ["REDIS_6_LATEST"] = "6.0.6"
    os.environ["MEMCACHED_LATEST"] = "1.6.6"
    os.environ["RABBITMQ_3_LATEST"] = "3.8.7"

    # export default services
    os.environ["DB"] = "psql"
    os.environ["ES"] = "es"
    os.environ["CACHE"] = "redis"

    # Elasticsearch
    os.environ["ES_VERSION"] = "7.2.0"
    # to override with latest version:
    # os.environ["ES_VERSION"] = os.environ["ES_7_LATEST"]

    # PostrgreSQL
    os.environ["PSQL_VERSION"] = "9.6"
    os.environ["PSQL_USER"] = "invenio"
    os.environ["PSQL_PASSWORD"] = "invenio"
    os.environ["PSQL_DB"] = "invenio"

    # MySQL
    os.environ["MYSQL_USER"] = "invenio"
    os.environ["MYSQL_PASSWORD"] = "invenio"
    os.environ["MYSQL_DB"] = "invenio"
    os.environ["MYSQL_ROOT_PASSWORD"] = "invenio"

