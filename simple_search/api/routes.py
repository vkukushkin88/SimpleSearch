from flask_restful import Api

from simple_search.api import controllers


def search_api(app):
    api = Api(app)
    routes(api)


def routes(api):
    api.add_resource(controllers.Add, '/add/')
    api.add_resource(controllers.Search, '/search/')

