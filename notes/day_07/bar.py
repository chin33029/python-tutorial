""" Bar """
from inventory import get_inventory, add_item, remove_item_by_name
# import inventory

if __name__ == "__main__":
    print('------------- INVENTORY -----------------')
    print(get_inventory())
    print('-----------------------------------------')

    # This first item we are adding already exists in the inventory
    add_item({'name': 'Titos', 'type': 'VODKA', 'price': 13.07})

    # This second item we are adding does not exist in the inventory yet
    add_item({'name': 'Absolute', 'type': 'VODKA', 'price': 11.27})

    print('------------- INVENTORY -----------------')
    print(get_inventory())
    print('-----------------------------------------')

    # Remove an item thatis in the list
    remove_item_by_name('Titos')

    print('------------- INVENTORY -----------------')
    print(get_inventory())
    print('-----------------------------------------')

    # Example of creating a dictionary from inputs and adding it to inventory
    ITEM_NAME = input('Name: ')
    ITEM_TYPE = input('Type: ')
    ITEM_PRICE = input('Price: ')

    add_item({'name': ITEM_NAME, 'type': ITEM_TYPE, 'price': ITEM_PRICE})

    print('------------- INVENTORY -----------------')
    print(get_inventory())
    print('-----------------------------------------')
