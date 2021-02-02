import logging
import os

api_version = "v1"
confs = {
    'PROD':'config.ProductionConfig',
    'DEV':'config.DevelopmentConfig',
    'TEST':'config.TestingConfig',
}

class BaseConfig(object):
    API_VERSION = api_version
    ELASTIC_HOST = os.environ.get('ELASTIC_HOST', 'localhost')
    ELASTIC_PORT = os.environ.get('ELASTIC_PORT', '9200')

class ProductionConfig(BaseConfig):
    DEBUG = False
    LOG_LEVEL = logging.INFO


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class TestingConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


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
