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
        # Sets game id
        payload['game_id'] = next_game_id
        # payload['board'] = Binary(pickle.dumps(board, protocol=0))
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

    def update_game_player_yellow(self, game_id, player_id):
        """ Assign Player Yellow with Player ID """
        game_result = self.collection.find_one({'game_id': int(game_id)},
                                               {'_id': 0})
        color = 'playerYellow'
        pstat = self.player_status_chk(player_id)
        gstat = self.game_status_chk(color, game_id, game_result)
        if pstat == player_id and gstat == game_id:
            self.collection.update_one({'game_id': int(game_id)},
                                       {'$set': {'playerYellow': player_id}})
            gstat_changer = self.game_status_changer(game_id)
            return {
                'message': f'Player {color} has been added by Player Number {player_id}  {gstat_changer}'
            }, 200
        return {
            'game': f"{pstat}   {gstat}"
        }, 400

    def update_game_player_red(self, game_id, player_id):
        """ Assign Player Red with Player ID """
        game_result = self.collection.find_one({'game_id': int(game_id)},
                                               {'_id': 0})
        color = 'playerRed'
        pstat = self.player_status_chk(player_id)
        gstat = self.game_status_chk(color, game_id, game_result)
        if pstat == player_id and gstat == game_id:
            self.collection.update_one({'game_id': int(game_id)},
                                       {'$set': {'playerRed': player_id}})

            gstat_changer = self.game_status_changer(game_id)
            return {
                'message': f'Player {color} has been added by Player Number {player_id}  {gstat_changer}'
            }, 200
        return {
            'game': f"{pstat}   {gstat}"
        }, 400

    def update_player_yellow_move(self, game_id, column_number):
        """ Updates board with player yellows move """
        result = self.collection.find_one({'game_id': int(game_id)},
                                          {'_id': 0})
        column_number = int(column_number)
        if result:
            turn = result['turn_count']
            if self.turn_chk(turn) is not True:
                board = result['board']
                player_id = result['playerYellow']
                if self.is_valid_location(board, column_number):
                    row = self.next_open_row(board, column_number)
                    self.play_drop(board, row, column_number, player_id)
                    self.collection.update_one({'game_id': int(game_id)},
                                               {'$set': {'board': board,
                                                         'playerUp': "Red's Turn"},
                                                '$inc': {'turn_count': 1}})
                    self.print_board(board)
                    if self.win_chk(board, player_id):
                        self.print_board(board)
                        print("game over")

                    return{
                        'message': f'Player {player_id} has moved Player Red is next',
                        'board': f'{board}',
                        'turn': f'Thast was {turn} next is {turn + 1}'
                        }, 200
                else:
                    return {
                        'message': f'Sorry Column {column_number} is full!'
                    }, 400
            else:
                return{
                    'message': f'Sorry its player Red turn'
                }, 400
        else:
            return{
                'message': f'Could not find game {game_id}'
            }, 400

    def update_player_red_move(self, game_id, column_number):
        """ Updates board with player reds move """  # TODO: has to check for players
        result = self.collection.find_one({'game_id': int(game_id)},
                                          {'_id': 0})
        column_number = int(column_number)
        if result:
            turn = result['turn_count']
            if self.turn_chk(turn) is True:
                board = result['board']
                player_id = result['playerRed']
                if self.is_valid_location(board, column_number):
                    row = self.next_open_row(board, column_number)
                    self.play_drop(board, row, column_number, player_id)
                    self.collection.update_one({'game_id': int(game_id)},
                                               {'$set': {'board': board,
                                                         'playerUp': "Yellow's Turn"},
                                                '$inc': {'turn_count': 1}})
                    self.print_board(board)
                    if self.win_chk(board, player_id):
                        self.print_board(board)
                        print("game over")
            
                    return {
                        'message': f'player {player_id} has moved Player Yellow is Next',
                        'board': f'{board}',
                        'turn': f'Thast was {turn} next is {turn + 1}'
                    }, 200
                else:
                    return {
                        'message': f'Sorry Column {column_number} is full! '
                    }, 400
            else:
                return {
                    'message': f'Sorry its player Yellows turn'
                }, 400
        else:
            return{
                'message': f'Could not find game {game_id}'
            }, 400




            
    @staticmethod
    def is_valid_location(board, column_number):
        """ Checks if Row is valid by search for 0 in column """
        if board[5][column_number] == 0:
            return True
        else:
            return False

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
            payload['playerUp'] = "Red goes First! "
        payload['playerUp'] = "Yellow goes First! "
   
    @staticmethod
    def turn_chk(turn):
        """Assigns turnchk value """
        if (turn % 2) == 0:
            return True
        return False

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

    def game_status_changer(self, game_id):
        """ Checks for Game Player Vacancy """
        result = self.get_one(game_id)
        yellow_stat = int(result['playerYellow'])
        red_stat = int(result['playerRed'])
        if yellow_stat != 0 and red_stat != 0:
            self.collection.update_one({'game_id': int(game_id)},
                                       {'$set': {"status": "IN_ACTION"}})
            return {
                'message': f"{yellow_stat} and {red_stat} are now playing"
            }, 201
        return {
            'message': f"Game still needs players"
        }, 200
    