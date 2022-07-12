from webargs import fields
from webargs.flaskparser import parser
from flask import jsonify, request
from flask.views import MethodView

from service import controller

header_schema = {
    "width": fields.Int(missing=None),
    "height": fields.Int(missing=None),
    "state": fields.List(fields.Int)
}


class CreateBoard(MethodView):

    def post(self):
        args = parser.parse(header_schema, request, location='json')
        if args["width"] is not None and args["height"] is not None:
            controller.create_board(args["width"], args["height"])
        else:
            controller.create_board(5, 5)
        return jsonify(controller.board.state.tolist())


class SetState(MethodView):

    def post(self):
        args = parser.parse(header_schema, request, location='json')
        try:
            controller.board.set_state(args["state"])
        except AttributeError:
            return "Initialise a board first"
        return jsonify(controller.board.state.tolist())


class Tick(MethodView):

    def get(self):
        controller.board.tick()
        return jsonify(controller.board.state.tolist())
