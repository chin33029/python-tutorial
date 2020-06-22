''' Example class '''
import logging

from util.db_util import DBUtil
from util.utils import snake_case


class Example():
    ''' Example class '''

    def __init__(self):
        self.class_name = type(self).__name__
        self.logger = logging.getLogger(self.class_name)
        self.collection_name = snake_case(self.class_name)
        self.collection = DBUtil().get_collection(self.collection_name)

    def add_item(self, item):
        ''' Add an item to the database '''
        self.collection.insert_one(item)
