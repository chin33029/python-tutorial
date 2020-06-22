""" Bottle class """
from service.item import Item


class Bottle(Item):
    ''' Bottle Class '''

    def __init__(self, n='UNDEFINED', t='UNDEFINED'):
        super(Bottle, self).__init__()
        self.type = t
        self.name = n
        self.size = 750
        self.quantity = 0

    def get_bottle(self):
        ''' return the bottle info as a dictionary item '''
        return {
            'name': self.name,
            'type': self.type,
            'price': self.price,
            'size': self.size,
            'quantity': self.quantity
        }

    def update_name(self, new_name):
        ''' Update a bottle name '''
        self.name = new_name

    def update_type(self, new_type):
        ''' Update a bottle type '''
        self.type = new_type.upper()

    def update_quantity(self, quantity):
        '''update quantity'''
        self.quantity = int(quantity)

    def update_size(self, new_size):
        ''' update size '''
        self.size = int(new_size)
