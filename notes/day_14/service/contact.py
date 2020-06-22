''' Contact class '''
import logging

from util.db_util import DBUtil
from util.utils import snake_case


class Contact():
    ''' Contact class '''

    def __init__(self):
        self.class_name = type(self).__name__  # Contact
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def add_item(self, item):
        ''' Add an item to the database '''
        if self.find_one(query={
                'firstName': item['firstName'],
                'lastName': item['lastName']}):
            self.logger.error('Contact already exists for %s %s',
                              item['firstName'], item['lastName'])
            return
        self.logger.info('Contact %s %s added successfully',
                         item['firstName'], item['lastName'])
        self.collection.insert_one(item)

    def find_one(self, query):
        ''' find a item in collection '''
        return self.collection.find_one(filter=query)

    def find_many(self, query):
        ''' find a item in collection '''
        return self.collection.find(filter=query)

    def delete_one(self, query):
        ''' delete an item from collection '''
        return self.collection.delete_one(filter=query)

    def delete_many(self, query):
        ''' delete an item from collection '''
        return self.collection.delete_many(filter=query)

    def update(self, query, update_dict):
        ''' update a item in the collection '''
        result = self.collection.update_one(filter=query, update=update_dict)
        if result.modified_count == 0:
            self.logger.warning('Nothing changed')
        else:
            self.logger.info('New -> %s', self.find_one(query=query))
