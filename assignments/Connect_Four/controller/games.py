"""Games Endpoint"""
from flask import request
from flask_restx import Namespace, Resource, fields, reqparse
from service.games import Games


NS = Namespace(
    'games',
    description='Operations related to Games'
)

PUT_PARSER = reqparse.RequestParser()
GET_PARSER = reqparse.RequestParser()
PUT_PARSER.add_argument(
    "color", default=None,
    choices=['yellow_player', 'red_player'],
    required=False,
    help='Assign player to color'
)
GET_PARSER.add_argument(
    "status", default=None,
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
        "player_yellow": fields.Integer(
            required=False,
            descrioption="//refer to player",
            default=None,
            example=0
        ),
        "player_red": fields.Integer(
            required=False,
            description="//refer to player",
            default=None,
            example=0
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
            default=None
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





# @NS.route("/<string:game_id>/<string:color>/<string:player_id>")
# class GamesPlayer(Resource):
#     """ Player Assignment """
#     @NS.doc(parser=PUT_PARSER)
#     def put(self, game_id, player_id):
#         """ Assigns PLayer to Color by Player Id"""
#         args = PUT_PARSER.parse_args()
#         print("Heeeeeeeeeeeeerrrrrrrrrrrrreeeeeeeeeeee")
#         return Games().update_game_player(game_id, args["color"], player_id)
        


@NS.route("/<string:game_id>/player-yellow/<string:player_id>")
class GamesPlayerYellow(Resource):
    """Player Yellow Added to Game Id """
    def put(self, game_id, player_id):
        """ Assigns GameID to Player Yellow """
        color = 'player_yellow'
        return Games().update_game_player(game_id, color, player_id)


@NS.route("/<string:game_id>/player-red/<string:player_id>")
class GamesPlayerRed(Resource):
    """Player Red Added to Gameid """
    def put(self, game_id, player_id):
        """ Assigns GameID to Player Red """
        color = 'player_red'
        return Games().update_game_player(game_id, color, player_id)


@NS.route("/<string:game_id>/player-yellow/player_id/column/<string:column_number>")
class GamesMovePlayerYellow(Resource):
    """ Player Yellow Move Placement"""
    def put(self, game_id, column_number):
        """ Column Play """
        color = 'player_yellow'
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
            return Games().update_player_move(game_id, color, column_number)


@NS.route("/<string:game_id>/player-red/player_id/column/<string:column_number>")
class GamesMovePlayerRed(Resource):
    """ Player Red Move Placement"""
    def put(self, game_id, column_number):
        """ Column Play """
        color = 'player_red'
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
            return Games().update_player_move(game_id, color, column_number)



