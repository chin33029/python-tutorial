""" Entry Point """
# from service.inventory import say_hello
# from data.inventory import INVENTORY
# import service.inventory as inv
from service.item import Item
from service.bottle import Bottle
from service.warehouse import Warehouse

if __name__ == "__main__":
    # print('Starting point')
    # inv.say_hello()
    # print(INVENTORY)
    ITEM = Item()
    print(ITEM)
    print(ITEM.get_price())
    ITEM.update_price(3.25)
    print(ITEM.get_price())
    print(ITEM)

    BOTTLE = Bottle()
    print(BOTTLE.get_bottle())
    BOTTLE.update_name('Stoli')
    print(BOTTLE.get_bottle())
    BOTTLE.update_price(10.00)
    print(BOTTLE.get_bottle())
    BOTTLE.update_type('vodka')
    print(BOTTLE.get_bottle())

    BOTTLE.update_size(1000)
    print(BOTTLE.get_bottle())
    BOTTLE.update_quantity(12)
    print(BOTTLE.get_bottle())

    WAREHOUSE = Warehouse()
    WAREHOUSE.add_bottle(BOTTLE)
    WAREHOUSE.add_bottle(Bottle(n='Dean', t='TEST'))
    WAREHOUSE.add_bottle(Bottle())
    WAREHOUSE.add_bottle(Bottle(t='RUM'))
    WAREHOUSE.add_bottle(
        Bottle(
            t=input('What type of liqour? ').upper()
        )
    )
    print(WAREHOUSE.get_inventory())

    # Item().get_price() # This is a new instance of Item FrontLeft (1.0)
    # Item().update_price(5.25) # Another instance  - FrontWheel (5.25)
    # Item().get_price() # Third instance   - BackLeft (1.0)

