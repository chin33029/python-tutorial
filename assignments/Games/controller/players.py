""" Movies Endpoint """
from flask import request
from flask_restx import Namespace, Resource, fields, reqparse

from service.players import Players


NS = Namespace(
    'players',
    description='Operations related to players'
)
GET_PARSER = reqparse.RequestParser()
GET_PARSER.add_argument(
    'level', choices=['Beginner',
                      'Novice',
                      'Intermediate',
                      'Advanced',
                      'Badass'],
    required=False, default=None)
GET_PARSER.add_argument(
    'state', choices=['IN_LOBBY',
                      'IN_GAME',
                      'OFFLINE'],
    required=False, default=None)


# regex code please
PLAYERS = NS.model(
    "Players", {
        "username": fields.String(
            required=True,
            description="username",
            example="username2"
        ),
        "password": fields.String(
            required=True,
            description="1 lowercase, 1 uppercase, 1 number, min 8 char, max 32 char",
            example="Password123",
            pattern=r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,32}$'
        ),
        "displayName": fields.String(
            required=True,
            description="CooL-Name",
            example="chinchilla2",
            pattern=r'^[a-zA-Z0-9]+([a-zA-Z0-9](_|-| )[a-zA-Z0-9])*[a-zA-Z0-9]+$'
        ),
        "avatar": fields.Url(
            # needs work for url
            required=False,
            default=None,
            description="Url for avatar",
            example="www.image.gif"
        ),
        "level": fields.String(
            required=False,
            default="Beginner",
            description="level",
            example="Beginner"
        ),
        "state": fields.String(
            required=False,
            default="OFFLINE",
            description="player state",
            example="IN_LOBBY, IN_GAME, OFFLINE",
            enum=['IN_LOBBY', 'IN_GAME', 'OFFLINE']
        ),
        "activeGameId": fields.String(
            required=False,
            default=None,
            example="1"
        ),
        # "friends": {
        #     "displayName": fields.String,
        #     "username": fields.String
        # }
     
    }
)

PUT_PLAYER_STATE = NS.model(
    "PlayerState", {
        "state": fields.String(
            required=False,
            default="OFFLINE",
            description="player state",
            example="IN_LOBBY, IN_GAME, OFFLINE",
            enum=['IN_LOBBY', 'IN_GAME', 'OFFLINE']
        ),
    }
)

PUT_PLAYER = NS.model(
    "Player", {
        "avatar": fields.Url(
            # needs work for url
            required=False,
            default=None,
            description="Url for avatar",
            example="www.image.gif"
        ),
        "level": fields.String(
            required=False,
            default="Beginner",
            description="level",
            example="Beginner"
        ),
        "state": fields.String(
            required=False,
            default="OFFLINE",
            description="player state",
            example="IN_LOBBY, IN_GAME, OFFLINE",
            enum=['IN_LOBBY', 'IN_GAME', 'OFFLINE']
        ),
        "activeGameId": fields.String(
            required=False,
            default=None,
            example="1"
        )

    }
)

# FRIENDS = NS.model('Player', {
#     "username": fields.String,
#     "displayName": fields.String,
#     "level": fields.String,
# })

# LIST_FRIENDS = NS.model('PlayerList', {
#           'players': fields.List(fields.Nested(FRIENDS))
#         })



@NS.route("")
class PlayersCollection(Resource):
    """ Player Collection methods """

    @NS.doc(parser=GET_PARSER)
    def get(self):
        """ Returns list of Players """
        args = GET_PARSER.parse_args()
        print(f'args={args}')
        return Players().get_all(args['level'], args['state'])

    @NS.expect(PLAYERS, validate=True)
    def post(self):
        """ Adds a new Player """
        return Players().create_one(request.get_json())


@NS.route("/<string:username>")
class PlayerItem(Resource):
    """ Username methods """

    def get(self, username):
        """ Returns a player with username """
        return Players().get_one(username)

    @NS.expect(PUT_PLAYER, validate=True)
    def put(self, username):
        """ Updates a player with username """
        return Players().update_one(username, request.json)

    def delete(self, username):
        """ Deletes a player with username """
        return Players().delete_one(username)


@NS.route("/<string:username>/state")
class PlayerStateItem(Resource):
    """Player State Methods"""

    def get(self, username):
        """gets state for username"""
        return Players().get_user_state(username)

    @NS.expect(PUT_PLAYER_STATE, validate=True)
    def put(self, username):
        """updates state of player"""
        return Players().update_one_state(username, request.json)