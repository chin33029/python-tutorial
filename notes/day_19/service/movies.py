''' Movies class '''
import logging
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from util.db_util import DBUtil
from util.utils import snake_case, load_json_schema


class Movies():
    ''' Movies class '''

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def get_all(self, genre=None, in_theaters=None):
        ''' get all movies '''
        self.logger.info('genre=%s in_theaters=%s', genre, in_theaters)
        self.logger.info(list(self.collection.find({})))

        # Add query parameters if they are passed in
        query = {}
        if genre:
            query['genre'] = genre
            self.logger.info('QUERY lookie like this: %s', query)
        if in_theaters is not None:  # Make sure we also add to query if False
            query['inTheaters'] = in_theaters
            self.logger.info('QUERY lookie like this: %s', query)

        return {
            'result': list(self.collection.find(query, {'_id': 0}))
        }, 200

    def get_one(self, name):
        ''' get one movie by name '''
        result = self.collection.find_one({'name': name}, {'_id': 0})
        if result:
            return result, 200
        return {'message': f'{name} not found'}, 404

    def create_one(self, payload):
        ''' Create an movie '''
        resp, code = self.validate_schema(payload)
        if code != 200:
            return resp, code

        self.collection.insert_one(payload)
        return {
            'message': f'Created movie: {payload}'
        }, 201

    def update_one(self, name, payload):
        ''' update one movie by name '''
        result = self.collection.find_one({'name': name}, {'_id': 0})

        if result:
            self.collection.update_one({"name": name}, {"$set": payload})
            return {'message': f'Updated {name}'}, 200
        return {
            'message': f'{name} not found'
        }, 404

    def delete_one(self, name):
        ''' delete one movie by name '''
        return {
            'message': f'Delete {name}'
        }, 200

    def validate_schema(self, payload):
        """ Validates application definiition against schema """
        schema = load_json_schema('movie-schema.json')

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
