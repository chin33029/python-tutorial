""" Inventory """
INVENTORY = [
    {'name': 'Stoli', 'type': 'VODKA', 'price': 123.07},
    {'name': 'Patron', 'type': 'TEQUILA', 'price': 124.97},
    {'name': 'Titos', 'type': 'VODKA', 'price': 13.07}
]


def get_inventory():
    """ This returns the inventory """
    return INVENTORY


def add_item(item):
    """ Add a new item to the inventory """
    # Check first if the item already exists in the inventory
    for i in get_inventory():
        if i['name'] == item['name']:
            print(f"[ERROR] item with name {i['name']} already exists")
            break
    else:
        print(f'[INFO] Adding item {item}')
        INVENTORY.append(item)
        # mongo.collection().insert_one(item)


def remove_item(item):
    """ Remove an item """
    INVENTORY.remove(item)


def remove_item_by_name(name):
    """ Remove an item with thename specified """
    item_found = False
    for item in INVENTORY.copy():
        if name == item['name']:
            item_found = True
            print(f'[INFO] Removing item {item}')
            remove_item(item)

    if not item_found:
        print(f'Sorry, we did not find {name} in inventory.')
