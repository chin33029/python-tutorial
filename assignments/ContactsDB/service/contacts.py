''' Contacts class '''

import logging
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from util.db_util import DBUtil
from util.utils import snake_case


class Contacts():
    ''' Contact class '''
    def __init__(self):
        self.class_name = type(self).__name__  # Contact
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)
  
    def get_all(self, phonetype_one=None, phonetype_two=None, phonetype_three=None):
        ''' get all items '''
        
        query = {}
        if phonetype_one:
            query['phonetype_one'] = phonetype_one
        if phonetype_two:
            query['phonetype_two'] = phonetype_two
        if phonetype_three:
            query['phonetype_three'] = phonetype_three
        
        return {
            'results': list(self.collection.find({}, {'_id': 0}))
            }, 200

    def get_one(self, name):
        ''' get one contact by name '''
        find_one = self.collection.find_one({'Name': name}, {'_id': 0})
        if find_one:
            return find_one
        return {
                'message': f'not found item {name}'
            }, 404

    def create_one(self, payload):
        ''' Create an contact '''
        find = self.collection.find_one(payload)
        if find:
            return {
                'message': f'Item {payload} already exists'
            }, 400
        self.collection.insert_one(payload)
        return {
            'message': f'Created item: {payload}',
            'name': f'{payload["Name"]}',
        }, 201

    def update_one(self, name, payload):
        ''' update one contact by name '''
        result = self.collection.find_one({'Name': name}, {'_id': 0})

        if result:
            self.collection.update_one({"Name": name}, {"$set": payload})
            return {'message': f'Updated {name}'}, 200
        return {
            'message': f'{name} not found'
        }, 404

    def delete_one(self, name):
        ''' delete one contact by name '''
        result = self.collection.delete_one({'Name': name})
        if result.deleted_count:
            return {'message': f'Deleted {name} successfully'}, 200
        return {'message': f'No contact found with name = {name}'}, 404

    def validate_schema(self, payload):
        """ Validates application definiition against schema """
        schema = load_json_schema('contact-schema.json')

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

