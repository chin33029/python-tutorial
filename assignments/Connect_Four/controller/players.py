"""Players Endpoints"""

from flask import request
from flask_restx import Namespace, Resource, fields, reqparse
from service.players import Players


NS = Namespace(
    'players',
    description='Operations related to Players'
)
GET_PARSER = reqparse.RequestParser()
GET_PARSER.add_argument(
    "status", choices=["OFFLINE", "LOBBY", "IN_GAME"],
    required=False,
    help="Player status"
)

PLAYER = NS.model(
    "Player", {
        "playerDisplayName": fields.String(
            required=True,
            description="Players Display Name",
            example="PlayerUno"
        ),
        "status": fields.String(
            required=False,
            description="Players Status",
            example="OFFLINE, LOBBY, IN_GAME",
            default=None
        )
    }
)


@NS.route("")
class PlayersCollection(Resource):
    """ Players Collection methods"""
    @NS.doc(parser=GET_PARSER)
    def get(self):
        """ Returns List of Players """
        args = GET_PARSER.parse_args()
        return Players().get_all(args["status"])

    @NS.expect(PLAYER)
    def post(self):
        """ Creates a new Player """
        return Players().create_one(request.get_json())


@NS.route("/<string:player_id>")
class Player(Resource):
    """ Player Methods """

    def get(self, player_id):
        """ Returns Player by Id number"""
        return Players().get_one_player_id(player_id)

    @NS.expect(PLAYER, validate=True)
    def put(self, player_id):
        """ Updates Player by player_id """
        return Players().update_one_by_id(player_id, request.json)


@NS.route("/<string:player_id>/status/<string:status_name>")
class PlayerStatus(Resource):
    """ Player Methods """

    def get(self, player_id):
        """ Returns Player by Id number"""
        return Players().get_one_player_id(player_id)

    @NS.expect(PLAYER, validate=True)
    def put(self, player_id):
        """ Updates Player by player_id """
        return Players().update_one_by_id(player_id, request.json)


