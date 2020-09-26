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
WIN_COUNT = 4


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
        print(board)
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
        print(type(board.tolist()))
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
        """ Assign Player Color with Player ID """
        game_result = self.collection.find_one({'game_id': int(game_id)},
                                               {'_id': 0})
        gstat = self.game_status_chk(color, game_id, game_result)
        pstat = self.player_status_chk(player_id)
        if pstat == player_id and gstat == game_id:
            self.collection.update_one({'game_id': int(game_id)},
                                       {'$set': {color: player_id}})
            Players().collection.update_one({'player_id': float(player_id)},
                                            {'$set': {"status": "IN_GAME"}}
                                            )
            gstat_changer = self.game_status_changer(game_id)
            return {
                'message':
                    f'Player {color} added [id={player_id}] {gstat_changer}'
            }, 200
        return {
            'game': f"{pstat}   {gstat}"
        }, 400

    def update_player_move(self, game_id, color, column_number):
        """ Updates board with player reds move """
        result = self.collection.find_one({'game_id': int(game_id)},
                                          {'_id': 0})
        player_id = result[color]
        column_number = int(column_number)
        board = result['board']
        turn = result['playerUp']
        turn_chk = self.turn_chk(turn,
                                 board,
                                 column_number,
                                 player_id,
                                 game_id,
                                 color,
                                 result
                                 )
        if result["status"] != "IN_ACTION":
            return {
                'message': f'Game {game_id} is not Available!'
            }, 400

        if turn_chk:
            print(self.print_board(board))
        return turn_chk

    def is_valid_location(self,
                          board,
                          column_number,
                          player_id,
                          game_id,
                          color,
                          result
                          ):
        """ Checks if Row is valid by search for 0 in column """
        if board[ROW_COUNT - 1][column_number] == 0:
            row = self.next_open_row(board, column_number)
            play = self.play_drop(board, row, column_number, player_id)
            next_up = self.nextup(color)
            self.collection.update_one(
                {'game_id': int(game_id)},
                {
                    '$set': {
                        'board': board,
                        'playerUp': next_up
                    },
                    '$inc': {'turn_count': 1}
                }
            )
            if self.win_chk(board, play) is True:
                self.ends_game(game_id, player_id, board, result)
                print("winner-----")
            return {
                "message": f"{color} moved {next_up} is next"
            }

        else:
            return {
                'message': f'Row is full at {column_number} !'
            }, 400

    @staticmethod
    def next_open_row(board, column_number):
        """ Looks for Next Available Row """
        print("next open --")
        for row in range(ROW_COUNT):
            if board[row][column_number] == 0:
                return row

    @staticmethod
    def play_drop(board, row, col, play):
        """ Places Board Play """
        print("play drop -- ")
        board[row][col] = play
        return play

    @staticmethod
    def print_board(board):
        """ Prints Board and flips """
        # board = np.fromiter(board)
        return np.flip(board, 0)

    @staticmethod
    def create_turn_counter(payload):
        """Creates a turn counter"""
        turn_count = random.randint(0, 50)
        payload['turn_count'] = turn_count
        if turn_count % 2 == 0:
            payload['playerUp'] = 'player_red'
        payload['playerUp'] = 'player_yellow'

    def turn_chk(self,
                 turn,
                 board,
                 column_number,
                 player_id,
                 game_id,
                 color,
                 result):
        """ Entry Point Checks for turn
        through color variable against turn """
        validate_location = self.is_valid_location(board,
                                                   column_number,
                                                   player_id,
                                                   game_id,
                                                   color,
                                                   result
                                                   )
        if color == turn:
            return validate_location

        else:
            return {
                "message": f"Sorry turn = {turn}!"
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
        yellow_stat = float(result['player_yellow'])
        red_stat = float(result['player_red'])
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
        player_result = Players().get_one_player_id(float(player_id))
        if isinstance(player_result, dict):
            player_status = player_result['status']
            if player_status == "LOBBY":
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
            game_status = float(game_result[color])
            if game_status == 0:
                return game_id
            return {
                "message": f"Sorry {player_color} taken for {game_id} !"
            }, 400
        return {
            "message": f"Sorry game id {game_id} could not be found!"
            }, 400

    def win_chk(self, board, play):
        """ Looks for Win """
        if self.win_chk_diag_down(board, play):
            return True
        if self.win_chk_diag_up(board, play):
            return True
        if self.win_chk_horizontals(board, play):
            return True
        if self.win_chk_verticals(board, play):
            return True

    def ends_game(self, game_id, player_id, board, result):
        """ Ends game Resets Players declares winner """
        self.reset_players(result)
        self.collection.update_one({"game_id": int(game_id)},
                                   {'$set': {'status': 'win',
                                             'player_yellow': 0,
                                             'player_red': 0,
                                             'winner': (player_id)}})
        print(self.print_board(board))
        return {
            'message': f'Winner!! {player_id}, has won!!',
            'Game Status': f'Game number {game_id} is over!!'
        }, 200

    @staticmethod
    def reset_players(result):
        """Resets Players to Lobby"""
        Players().collection.update_one(
            {"player_id": int(result["player_yellow"])},
            {'$set': {'status': 'IN_LOBBY'}})
        Players().collection.update_one(
            {"player_id": int(result["player_red"])},
            {'$set': {'status': 'IN_LOBBY'}})

    @staticmethod
    def win_chk_verticals(board, play):
        """Win Check"""
        print(f"---play = {play}")
        print("hecking verticalsttttttt")
        # Checks Vertical Wins
        for col in range(COL_COUNT):
            for row in range(ROW_COUNT - (WIN_COUNT - 1)):
                print("inside for vertical loop")
                if board[row][col] == play:
                    win_cycle = 1
                    while True:
                        print(f"{row} --{col}")
                        row += 1
                        if board[row][col] == play:
                            win_cycle += 1
                            if win_cycle == WIN_COUNT:
                                print("win")
                                return True
                        if board[row][col] != play:
                            break

    @staticmethod
    def win_chk_horizontals(board, play):
        """Checks the Vertical wind"""
        # Checks Horizontal Wins
        for col in range(COL_COUNT - (WIN_COUNT - 1)):
            for row in range(ROW_COUNT):
                if board[row][col] == play:
                    win_cycle = 1
                    while True:
                        col += 1
                        if board[row][col] == play:
                            win_cycle += 1
                            if win_cycle == WIN_COUNT:
                                print("win")
                                return True
                        if board[row][col] != play:
                            break

    @staticmethod
    def win_chk_diag_down(board, play):
        """Checks Diagonal Win top to Bottom"""
        #  check diagonal top down
        for col in range(COL_COUNT - (WIN_COUNT - 1)):
            for row in range(ROW_COUNT - (WIN_COUNT - 1)):
                if board[row][col] == play:
                    win_cycle = 1
                    while True:
                        col += 1
                        row += 1
                        if board[row][col] == play:
                            win_cycle += 1
                            if win_cycle == WIN_COUNT:
                                print("win")
                                return True
                        if board[row][col] != play:
                            break

    @staticmethod
    def win_chk_diag_up(board, play):
        """Check Diagonal win Bottom to Top"""
        #  check diagonal bottom up
        for col in range(COL_COUNT - (WIN_COUNT - 1)):
            for row in range((WIN_COUNT - 1), ROW_COUNT):
                if board[row][col] == play:
                    win_cycle = 1
                    while True:
                        row -= 1
                        col += 1
                        if board[row][col] == play:
                            win_cycle += 1
                            if win_cycle == WIN_COUNT:
                                print("win")
                                return True
                        if board[row][col] != play:
                            break
