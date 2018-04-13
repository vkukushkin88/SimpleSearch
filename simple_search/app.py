
import logging

from flask import Flask

from simple_search.db.models import db, TblTextContainer
from simple_search.api.routes import search_api
import flask_whooshalchemy as wa


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # load configuration
    app.config.from_object('simple_search.config.Config')

    # setup logging
    logging.basicConfig(
        level='DEBUG' if app.config['LOG_LEVEL'] else 'INFO',
        format=app.config['LOG_FORMAT'],
        datefmt=app.config['LOG_DATEFMT']
    )

    # setup db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # init index
    wa.whoosh_index(app, TblTextContainer)

    # initialize APIs
    search_api(app)

    return app
