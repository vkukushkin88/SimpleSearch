
import logging

from flask import Flask

from simple_search.api.routes import search_api
from simple_search.tools.file_storage import FileStorage
from simple_search.tools.trie_index import TrieIndex


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

    # init custom index
    index = TrieIndex(app.config)
    fs = FileStorage(index, app.config)
    app.storage = fs
    app.storage.reindexing()

    # initialize APIs
    search_api(app)

    return app
