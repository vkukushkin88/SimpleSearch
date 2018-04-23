import logging

from flask import request, jsonify, Response
from flask import current_app as app
from flask_restful import Resource, abort


logger = logging.getLogger(__name__)


class Add(Resource):

    def post(self):
        request_data = request.get_json()
        new_record = request_data.get('content')
        if new_record:
            return app.storage.add(new_record), 201
        else:
            logger.error('Missed required key `content`.')
            return abort(400, message='Missed required key `content`.')


class Search(Resource):

    def get(self):
        return {
            'results': app.storage.get_by_keyword(
                request.args.get('query', '*'))
        }
