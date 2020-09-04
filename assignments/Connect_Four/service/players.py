''' Players class '''
import logging
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from util.db_util import DBUtil
from util.utils import snake_case
from util.utils import load_json_schema


class Players():
    ''' Players class '''

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def get_all(self, status=None):
        ''' Gets all Players '''
        query = {}
        if status:
            query["status"] = status
        return {
            'result': list(self.collection.find(query, {'_id': 0}))
        }, 200

    def get_one_player_id(self, player_id):
        ''' Gets one player by player_id '''
        find_one = self.collection.find_one({'player_id': int(player_id)},
                                            {'_id': 0})
        if find_one:
            return find_one
        return {
            'message': f'Player ID number {player_id} not found'
        }, 404

    def create_one(self, payload):
        '''Creates a Player '''
        chk_display_name = self.collection.find_one(
            {'playerDisplayName': payload['playerDisplayName']}
            )
        if chk_display_name:
            return {
                'message': f"Display Name {payload['playerDisplayName']} already exists!"
            }, 409

        resp, code = self.validate_schema(payload)
        if code != 200:
            return resp, code
        # New player_id
        result = list(self.collection.find(
            {'player_id': {'$ne': None}}, {'_id': 0, 'player_id': 1}
            ).sort('player_id', -1).limit(1))
        if result:
            next_player_id = int(result[0]['player_id']) + 1
        else:
            next_player_id = 1
        # Sets the player_id
        payload['player_id'] = next_player_id
        self.collection.insert_one(payload)
        return {
            'message': f'Created player: {payload}'
        }, 201

    def update_one_by_id(self, player_id, payload):
        """ Updates Player by player_id """
        result = self.collection.find_one({'player_id': int(player_id)},
                                          {'_id': 0}
                                          )
        if result:
            self.collection.update_one({'player_id': int(player_id)},
                                       {'$set': payload})
            return {
                'message': f'Updated Player ID {player_id} {payload}'
            }, 200
        return {
            'message'
        }

    def validate_schema(self, payload):
        """ Validates application definiition against schema """
        schema = load_json_schema('player-schema.json')

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
