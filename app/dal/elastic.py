import logging

from elasticsearch import Elasticsearch
from flask import json


class ElasticUtil(object):

    def __init__(self):
        self.es = None
        self.rep = None

    def connect_elasticsearch(self, elastic_host, elastic_port):
        if not self.es:
            _es = None
            _es = Elasticsearch([{'host': elastic_host, 'port': elastic_port}])
            if _es.ping():
                logging.info('Elastic connected!')
                self.es = _es
            else:
                logging.info('Cannot ping Elastic node!')
            return _es

    def create_index(self, index_name='main', type_name: str = '_doc', body=None):
        if body is None:
            body = {}
        created = False
        # index settings
        settings = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0,
            },
            "mappings": {
                "dynamic": "strict",
                "properties": body['properties']
            }
        }

        try:
            if not self.es.indices.exists(index_name):
                # Ignore 400 means to ignore "Index Already Exist" error.
                self.es.indices.create(index=index_name, body=settings)
                logging.info('Index created')
            created = True
        except Exception as ex:
            logging.error(str(ex))
        finally:
            return created

    @property
    def repository(self):
        if self.es:
            if not self.rep:
                self.rep = ElasticRepository(self.es)
            return self.rep
        else:
            logging.error('Connection is not established!')


class ElasticRepository(object):

    def __init__(self, esc):
        self.esc = esc

    def save(self, obj):
        try:
            outcome = self.esc.index(index='main', body=json.dumps(obj))
        except Exception as ex:
            logging.error(str(ex))
