''' Contact class '''
import logging

from util.db_util import DBUtil
from util.utils import snake_case


class Contact():
    ''' Contact class '''

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def add_item(self, item):
        ''' Add an item to the database '''
        self.collection.insert_one(item)

    def find_one_item(self, query):
        ''' find a item in collection '''
        return self.collection.find_one(filter=query)

    def find_many_item(self, query):
        ''' find a item in collection '''
        return self.collection.find_many(filter=query)

    def add_multiple(self, lists):
        '''insert multiple posts or documents'''
        return self.collection.insert_many(documents=lists)

    def find_all(self):
        '''returns all documents or a collection'''
        results = self.collection.find({})
        for result in results:
            print(result)
    # def find_multiple(self, results, result):
    #     '''finds multiple documents'''
    #     results = self.collection.find(result)
    #     for result in results:
    #         return results

    def delete_one_item(self, delt): # what is the filter from
        '''delete one item'''
        return self.collection.delete_one(filter=delt)

    def delete_clear(self):
        '''clear database'''
        return self.collection.delete_many({})

    def update_first_name(self, firstName):
        
        change = input('New name? ')
        return self.collection.update_one({'firstName': firstName}, {'$set': {'firstName': change}})


    



