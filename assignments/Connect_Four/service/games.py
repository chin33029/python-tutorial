'''Games class '''
import random
import logging
import numpy as np
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from service.players import Players

from util.db_util import DBUtil
from util.utils import snake_case
from util.utils import load_json_schema
ROW_COUNT = 6
COL_COUNT = 7


class Games():
    ''' Games class '''

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)
        self.board = None

    def get_all(self, status=None):
        ''' get all Games '''
        query = {}
        # board = pickle.loads(record['board'])
        if status:
            query["status"] = status
        return {
            'result': list(self.collection.find(query, {'_id': 0}))
        }, 200

    def get_one(self, game_id):
        ''' Gets one game by game_id '''
        find_one = self.collection.find_one({'game_id': int(game_id)},
                                            {'_id': 0})
        if find_one:
            return find_one
        return {
            'message': f'Game ID number {game_id} not found'
        }, 404

    def create_one(self, payload):
        '''Create a Game'''
        board = np.zeros((ROW_COUNT, COL_COUNT))
        resp, code = self.validate_schema(payload)
        if code != 200:
            return resp, code
        # New game_id
        result = list(self.collection.find(
            {'game_id': {'$ne': None}}, {'_id': 0, 'game_id': 1}
            ).sort('game_id', -1).limit(1))
        if result:
            next_game_id = int(result[0]['game_id']) + 1
        else:
            next_game_id = 0
        payload['game_id'] = next_game_id
        payload['board'] = board.tolist()
        self.create_turn_counter(payload)
        self.collection.insert_one(payload)
        return {
            'message': f'Created game: {payload}'
        }, 201

    def update_one(self, game_id, payload):
        ''' updates one game by game_id '''
        result = self.collection.find_one({'game_id': int(game_id)},
                                          {'_id': 0})
        if result:
            self.collection.update_one({'game_id': int(game_id)},
                                       {'$set': payload})
            return {'message': f'Updated Game ID{game_id} {payload}'}, 200
        return {
            'message': f'Game ID {game_id}, not found'
        }, 404

    def delete_one(self, game_id):
        '''delete a Game by game_id'''
        result = self.collection.delete_one({'game_id': int(game_id)})
        if result.deleted_count:
            self.collection.delete_one({'game_id': game_id})
            return {'message': f'Deleted Game ID{list(game_id)}'}, 200
        return {'message': f'No game with Game ID{game_id}found'}, 404

    def validate_schema(self, payload):
        """ Validates application definiition against schema """
        schema = load_json_schema('game-schema.json')

        try:
            validate(payload, schema)
        except ValidationError as v_err:
            self.logger.warning('Schema validation error: %s', v_err)
            return {
                'error': 'Failed schema validation',
                'message': v_err.message,
                'data': payload
            }, 422
        except Exception as ex:  # pylint: disable=broad-except
            self.logger.error('Unknown schema validation error: %s', ex)
            return {
                'error': 'Unkown schema validation',
                'message': ex,
                'data': payload
            }, 400
        return {
            'message': 'Application defininion passed schema validation'
        }, 200

    def update_game_player(self, game_id, color, player_id):
        """ Assign Player Red with Player ID """
        game_result = self.collection.find_one({'game_id': int(game_id)},
                                               {'_id': 0})
        pstat = self.player_status_chk(player_id)
        gstat = self.game_status_chk(color, game_id, game_result)
        if pstat == player_id and gstat == game_id:
            self.collection.update_one({'game_id': int(game_id)},
                                       {'$set': {color: player_id}})

            gstat_changer = self.game_status_changer(game_id)
            return {
                'message': f'Player {color} has been added by Player Number {player_id}  {gstat_changer}'
            }, 200
        return {
            'game': f"{pstat}   {gstat}"
        }, 400



    def update_player_move(self, game_id, color, column_number):
        """ Updates board with player reds move """  # TODO: has to check for players
        result = self.collection.find_one({'game_id': int(game_id)},
                                          {'_id': 0})
        player_id = result[color]
        column_number = int(column_number)
        board = result['board']
        turn_chk = self.turn_chk(result, color)
        valid_row = self.is_valid_location(board, column_number)
        row = self.next_open_row(board, column_number)
        next_up = self.nextup(color)
        if turn_chk is True:
            if valid_row is True:
                self.play_drop(board, row, column_number, player_id)
                self.collection.update_one({'game_id': int(game_id)},
                                           {'$set': {'board': board,
                                                     'playerUp': next_up},
                                            '$inc': {'turn_count': 1}})
                self.print_board(board)
                print(board)
                if self.win_chk(board, player_id):
                    self.print_board(board)
                    print("gameover------------")
                return {
                    'message': f'Player {player_id} has moved {next_up} is next',
                    'board': f'{board}'
                }, 200
                
            else:
                return self.is_valid_location(board, column_number)
        else:
            return turn_chk

        


            
    @staticmethod
    def is_valid_location(board, column_number):
        """ Checks if Row is valid by search for 0 in column """
        if board[5][column_number] == 0:
            return True
        else:
            return {
                'message': f'Row is full at {column_number} !'
            }, 400

    @staticmethod
    def next_open_row(board, column_number):
        """ Looks for Next Available Row """
        for row in range(ROW_COUNT):
            if board[row][column_number] == 0:
                return row

    @staticmethod
    def play_drop(board, row, col, play):
        """ Places Board Play """
        board[row][col] = play

    @staticmethod
    def print_board(board):
        """ Prints Board and flips """
        return (np.flip(board, 0))

    @staticmethod
    def create_turn_counter(payload):
        """Creates a turn counter"""
        turn_count = random.randint(0, 50)
        payload['turn_count'] = turn_count
        if turn_count % 2 == 0:
            payload['playerUp'] = 'player_red'
        payload['playerUp'] = 'player_yellow'
   
    @staticmethod
    def turn_chk(result, color):
        """Assigns turnchk value """
        turn = result['playerUp']
        if color == turn:
            return True
        return {
            'message': f"Sorry it is {turn}'s turn! "
        }, 400

    @staticmethod
    def nextup(color):
        """ Tracks next Player """
        if color == 'player_red':
            return 'player_yellow'
        if color == 'player_yellow':
            return 'player_red'

    def game_status_changer(self, game_id):
        """ Checks for Game Player Vacancy """
        result = self.get_one(game_id)
        yellow_stat = int(result['player_yellow'])
        red_stat = int(result['player_red'])
        if yellow_stat != 0 and red_stat != 0:
            self.collection.update_one({'game_id': int(game_id)},
                                       {'$set': {"status": "IN_ACTION"}})
            return {
                'message': f"{yellow_stat} and {red_stat} are now playing"
            }, 201
        return {
            'message': f"Game still needs players"
        }, 200

    @staticmethod
    def player_status_chk(player_id):
        """ Checks player Status to add to game """
        # Checks if player is in lobby and returns the id if eligible if not returns resp
        player_result = Players().get_one_player_id(int(player_id))
        if isinstance(player_result, dict):
            player_status = player_result['status']
            if player_status == "LOBBY":
                Players().collection.update_one({'player_id': int(player_id)},
                                                {'$set': {"status": "IN_GAME"}})
                return player_id
            return {
                "message": f"Player {player_id} is not eligible to join"
            }, 400
        return {
                "message": f"Player {player_id} could not be found!"
            }, 400

    @staticmethod
    def player_status_chk(player_id):
        """ Checks player Status to add to game """
        # Checks if player is in lobby and returns the id if eligible if not returns resp
        player_result = Players().get_one_player_id(int(player_id))
        if isinstance(player_result, dict):
            player_status = player_result['status']
            if player_status == "LOBBY":
                Players().collection.update_one({'player_id': int(player_id)},
                                                {'$set': {"status": "IN_GAME"}})
                return player_id
            return {
                "message": f"Player {player_id} is not eligible to join"
            }, 400
        return {
                "message": f"Player {player_id} could not be found!"
            }, 400

    @staticmethod
    def game_status_chk(color, game_id, game_result):
        """Checks game Status to add player red"""
        # Checks if game exists and if player spot is empty
        player_color = color
        if game_result:
            game_status = int(game_result[color])
            if game_status == 0:
                return game_id
            return {
                "message": f"Sorry player {player_color} spot is already taken for game id {game_id} !"
            }, 400
        return {
                "message": f"Sorry game id {game_id} could not be found!"
            }, 400

    @staticmethod
    def win_chk(board, play):
        """ Looks for Win """
        # check horizontals
        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT):
                if board[r][c] == play and board[r][c+1] == play and board[r][c+2] == play and board[r][c+3]:
                    return True
        # check verticles
        for c in range(COL_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == play and board[r+1][c] == play and board[r+2][c] == play and board[r+3][c]:
                    return True

        #   check diag bottom left top right
        for c in range(COL_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == play and board[r+1][c+1] == play and board[r+2][c+2] == play and board[r+3][c+3]:
                    return True

        #   check diag top left bottom right
        for c in range(COL_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if board[r][c] == play and board[r-1][c+1] == play and board[r-2][c+2] == play and board[r-3][c+3]:
                    return True