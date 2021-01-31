import logging
import os

api_version = "v1"


class BaseConfig(object):
    DEBUG = False
    API_VERSION = api_version
    ELASTIC_HOST = os.environ.get('ELASTIC_HOST', 'localhost')
    ELASTIC_PORT = os.environ.get('ELASTIC_PORT', '9200')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    API_VERSION = api_version
    ELASTIC_HOST = os.environ.get('ELASTIC_HOST', 'localhost')
    ELASTIC_PORT = os.environ.get('ELASTIC_PORT', '9200')


class TestingConfig(BaseConfig):
    DEBUG = True
    API_VERSION = api_version
    ELASTIC_HOST = os.environ.get('ELASTIC_HOST', 'localhost')
    ELASTIC_PORT = os.environ.get('ELASTIC_PORT', '9200')


elastic_commands = {
    'texts': {
        "dynamic": "strict",
        "properties": {
            "type": {"type": "keyword"},
            "body": {"type": "text"},
            "key_phrases": {"type": "text"},
        }
    },

}
