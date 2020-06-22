''' Example class '''
import logging

from util.db_util import DBUtil
from util.utils import snake_case


class Contact():
    ''' Example class '''

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def add_item(self, item):
        ''' Add an item to the database '''
        self.collection.insert_one(item)

    def find_item(self, query):
        '''find an item'''
        return self.collection.find_one(filter=query)

    def delete_item(self, query):
        return self.collection.delete_one(filter=query)
        