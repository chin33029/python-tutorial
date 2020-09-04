"""Games Endpoint"""
from flask import request
from flask_restx import Namespace, Resource, fields, reqparse
from service.games import Games


NS = Namespace(
    'games',
    description='Operations related to Games'
)
GET_PARSER = reqparse.RequestParser()
GET_PARSER.add_argument(
    "status", default='NOT_STARTED',
    choices=['NOT_STARTED', 'WIN', 'TIE',
             'IN_ACTION', 'INVALID_MOVE', 'INVALID_PLAYER'],
    required=True,
    help='Game status fields'
)

GAME = NS.model(
    "Game", {
        "message": fields.String(
            required=False,
            example="details"
        ),
        "winner": fields.String(
            required=True,
            description="//refer player",
            default=None,
            example="None"
        ),
        "playerRed": fields.Integer(
            required=False,
            description="//refer to player",
            default=None,
            example=0
        ),
        "playerYellow": fields.Integer(
            required=False,
            description="//refer to player",
            default=None,
            example=0,
        ),
        "playerUp": fields.String(
            required=False,
            description="lets us know what player is next",
            default=None,
            example="player yellow or orange"
        ),
        "status": fields.String(
            required=True,
            description="Game status",
            example="NOT_STARTED WIN TIE IN_ACTION INVALID_MOVE INVALID_PLAYER",
            default="NOT_STARTED"
        ),
    
    }
)


@NS.route("")
class GamesCollection(Resource):
    """ Games Collection methods """
    @NS.doc(parser=GET_PARSER)
    def get(self):
        """ Returns List of Games """
        args = GET_PARSER.parse_args()
        return Games().get_all(args["status"])

    @NS.expect(GAME, validate=True)
    def post(self):
        """ Creates a new Game """
        return Games().create_one(request.get_json())


@NS.route("/<string:game_id>")
class Game(Resource):
    """ Game methods """

    def get(self, game_id):
        """ Returns Game by Id number """
        return Games().get_one(game_id)

    @NS.expect(GAME, validate=True)
    def put(self, game_id):
        """ Updates Game by Id number """
        return Games().update_one(game_id, request.json)

    def delete(self, game_id):
        """ Deletes Game by Id number """
        return Games().delete_one(game_id)


@NS.route("/<string:game_id>/player-yellow/<string:player_id>")
class GamesPlayerYellow(Resource):
    """Player Yellow Added to Game Id """
    def put(self, game_id, player_id):
        """ Assigns GameID to Player Yellow """
        return Games().update_game_player_yellow(game_id, player_id)


@NS.route("/<string:game_id>/player-red/<string:player_id>")
class GamesPlayerRed(Resource):
    """Player Red Added to Gameid """
    def put(self, game_id, player_id):
        """ Assigns GameID to Player Red """
        return Games().update_game_player_red(game_id, player_id)


@NS.route("/<string:game_id>/player-yellow/player_id/column/<string:column_number>")
class GamesMovePlayerYellow(Resource):
    """ Player Yellow Move Placement"""
    def put(self, game_id, column_number):
        """ Column Play """
        try:
            column_number = int(column_number)
        except ValueError:
            return {
                'message': f'{column_number} is not a number! '
            }, 400
        if not 0 <= column_number <= 6:
            return {
                'message': f'Column {column_number} is not a valid play! '
            }, 400
        else:
            return Games().update_player_yellow_move(game_id, column_number)


@NS.route("/<string:game_id>/player-red/player_id/column/<string:column_number>")
class GamesMovePlayerRed(Resource):
    """ Player Red Move Placement"""
    def put(self, game_id, column_number):
        """ Column Play """
        try:
            column_number = int(column_number)
        except ValueError:
            return {
                'message': f'Column {column_number} is not a number! '
            }, 400
        if not 0 <= column_number <= 6:
            return {
                'message': f'Column {column_number} is not a valid play! '
            }, 400
        else:
            return Games().update_player_red_move(game_id, column_number)



