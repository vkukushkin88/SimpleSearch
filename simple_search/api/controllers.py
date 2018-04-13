import logging

from flask import request, jsonify, Response
from flask_restful import Resource, abort

from simple_search.db.models import TblTextContainer


logger = logging.getLogger(__name__)


class Add(Resource):

    def post(self):
        request_data = request.get_json()
        new_record = request_data.get('content')
        if new_record:
            return TblTextContainer.add(new_record).to_dict(), 201
        else:
            return abort(400, message='Missed required key `content`.')


class Search(Resource):

    def get(self):
        return [res.to_dict() for res in TblTextContainer.get_by_text(
            request.args.get('query'))], 200
