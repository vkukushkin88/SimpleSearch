import os
import logging

from flask import Flask

from simple_search.db.models import db
from simple_search.api.routes import search_api


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # load configuration
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])

    # setup logging
    logging.basicConfig(
        level='DEBUG' if app.config['LOG_LEVEL'] else 'INFO',
        format=app.config['LOG_FORMAT'],
        datefmt=app.config['LOG_DATEFMT']
    )

    # setup db
    db.init_app(app)

    # initialize APIs
    search_api(app)

    return app
