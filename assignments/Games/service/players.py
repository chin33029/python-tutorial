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
        self.class_name = type(self).__name__  # Contact
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def get_all(self, level=None, state=None):
        ''' get all items '''
        self.logger.info('level=%s state=%s', level, state)
        self.logger.info(list(self.collection.find({})))
        query = {}
        if level:
            query['level'] = level
            self.logger.info('QUERY %s', query)
        if state:
            query['state'] = state
            self.logger.info('QUERY %s', query)

        return {
            'results': list(self.collection.find(query, {'_id': 0}))
            }, 200

    def get_one(self, username):
        ''' gets player by username '''
        find_one = self.collection.find_one({'username': username},
                                            {'_id': 0})
        if find_one:
            return find_one
        return {'message': f'UserName {username} not found'}, 404

    def get_user_state(self, username):
        '''gets a userstate'''
        results = self.collection.find({'username': username},
                                            {'_id': 0})
        if results:
            for result in results:
                return result['state'], 200
        return {'message': f'Contact Username State {username} not found '}, 404

    def create_one(self, payload):
        ''' Create an username '''
        find_username = self.collection.find_one({'username': payload['username']},
                                            {'_id': 0})
        find_displayname = self.collection.find_one({'displayName': payload['displayName']},
                                            {'_id': 0})
            
        if find_displayname:
            return {
                'message': f'{payload["displayName"]} already exists'
            }, 409
        
        if find_username:
            return {
                'message': f'{payload["username"]} already exists'
            }, 409
        resp, code = self.validate_schema(payload)
        if code != 200:
            return resp, code
        self.collection.insert_one(payload)
        return {
            'message': f'Created Username: {payload}'
        }, 201

    def update_one(self, username, payload):
        ''' updates player by username'''
        result = self.collection.find_one({'username': username},
                                          {'_id': 0})
        print(result)
        if result:
            self.collection.update_one({"username": username},
                                       {"$set": payload})
            return {'message': f'Updated {username}'}, 200
        return {
            'message': f'Player {username} not found'
        }, 404

    def update_one_state(self, username, state):
        ''' updates player state by username '''
        results = self.collection.find_one({"username": username}, {'_id': 0})

        if results:
            self.collection.update_one({"username": username},
                                       {"$set": state})
            return {'message': f'Updated {username}'}, 200

        return {
            'message': f'Player {username} not found'
        }, 404

    def delete_one(self, username):
        ''' deletes player by username '''
        result = self.collection.delete_one({'username': username})
        if result:
            return {'message': f'Deleted {username} successfully'}, 200
        return {'message': f'No contact found with name = {username}'}, 404

    def validate_schema(self, payload):
        """ Validates application definiition against schema """
        schema = load_json_schema('username-schema.json')

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
