import logging

from flask import Flask

from extensions import *
from config import elastic_commands, confs


def create_app(env='DEV') -> Flask:
    app = Flask(__name__)
    app.config.from_object(confs[env])
    cfg = app.config

    logging.basicConfig(level=cfg['LOG_LEVEL'])

    # Initialise extensions
    es_util.connect_elasticsearch(cfg['ELASTIC_HOST'], cfg['ELASTIC_PORT'])
    es_util.create_index('es', body=elastic_commands['texts'])

    with app.app_context():
        from .api.controllers import api
        app.register_blueprint(api, url_prefix=f"/api/{cfg['API_VERSION']}")
    return app
