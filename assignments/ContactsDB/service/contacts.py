''' Contacts class '''

import logging
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from util.db_util import DBUtil
from util.utils import snake_case
from util.utils import load_json_schema


class Contacts():
    ''' Contact class '''
    def __init__(self):
        self.class_name = type(self).__name__  # Contact
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)
  
    def get_all(self,
                phonetype_one=None,
                phonetype_two=None,
                phonetype_three=None,
                first_name=None,
                last_name=None):
        ''' get all items '''
        
        query = {}
        if phonetype_one:
            query["phonetypeOne"] = phonetype_one
        if phonetype_two:
            query["phonetypeTwo"] = phonetype_two
        if phonetype_three:
            query["phonetypeThree"] = phonetype_three
        if first_name:
            query["firstName"] = first_name
        if last_name:
            query["lastName"] = last_name

        print(query)
        return {
            'results': list(self.collection.find(query, {'_id': 0}))
            }, 200

    def get_one(self, contact_id):
        ''' get one contact by contact_Id '''
        find_one = self.collection.find_one({'contact_id': int(contact_id)},
                                            {'_id': 0})
        if find_one:
            return find_one
        return {
                'message': f'Contact Id number {contact_id} not found'
            }, 404

    def create_one(self, payload):
        ''' Create an contact '''
        
        resp, code = self.validate_schema(payload)
        if code != 200:
            return resp, code
        # New Contact ID Formula
        result = list(self.collection.find(
            {'contact_id': {'$ne': None}}, {'_id': 0, 'contact_id': 1}
            ).sort('contact_id', -1).limit(1))
        if result:
            next_contact_id = int(result[0]['contact_id']) + 1
        else:
            next_contact_id = 0
        # Sets new Contact ID
        payload['contact_id'] = next_contact_id
        self.collection.insert_one(payload)
        return {
            'message': f'Created contact: {payload}'
        }, 201

    def update_one(self, contact_id, payload):
        ''' update one contact by name '''
        result = self.collection.find_one({'contact_id': int(contact_id)},
                                          {'_id': 0})

        if result:
            self.collection.update_one({"contact_id": int(contact_id)},
                                       {"$set": payload})
            return {'message': f'Updated {contact_id}'}, 200
        return {
            'message': f'Contact number {contact_id} not found'
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

