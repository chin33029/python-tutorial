""" Item class """


class Item():
    ''' Item class '''

    def __init__(self):
        self.price = 1.0

    def get_price(self):
        ''' return the price of the item '''
        return self.price

    def update_price(self, new_price):
        ''' update the price for the item '''
        self.price = new_price



# The init stands for initialization.
# You are initializing the class with some variables that you may use in the methods within the class
# A method is the same as a function... but inside a class.
#   The first argument for a method should always be self

