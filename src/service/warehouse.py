""" Warehouse Class """
from service.bottle import Bottle


class Warehouse():
    ''' Warehouse class '''

    def __init__(self):
        self.items = []

    def add_bottle(self, bottle):
        ''' add a bottle to the warehouse '''
        if not isinstance(bottle, Bottle):
            print('[ERROR] item is not of type Bottle')
            return
        self.items.append(bottle.get_bottle())

    def get_inventory(self):
        ''' return inventory items '''
        return self.items
