''' Movies class '''

import logging

from util.db_util import DBUtil
from util.utils import snake_case


class Movies():
    ''' Items class '''
    def __init__(self):
        self.class_name = type(self).__name__  # Contact
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)
  
    def get_all(self):
        ''' get all items '''
        
        return {
            'results': list(self.collection.find({}, {'_id': 0}))
            }, 200

    def get_one(self, name):
        ''' get one item by name '''
        find_one = self.collection.find_one({'name': name}, {'_id': 0})
        if find_one:
            return find_one
        return {
                'message': f'not found item {name}'
            }, 404

    def create_one(self, payload):
        ''' Create an movie '''
        find = self.collection.find_one(payload)
        if find:
            return {
                'message': f'Item {payload} already exists'
            }, 400
        self.collection.insert_one(payload)
        return {
            'message': f'Created item: {payload}',
            'itemName': f'{payload["name"]}',
            'itemGenre': f'{payload["genre"]}',
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
        result = self.collection.delete_one({'name': name})
        if result.deleted_count:
            return {'message': f'Deleted {name} successfully'}, 200
        return {'message': f'No movie found with name = {name}'}, 404
