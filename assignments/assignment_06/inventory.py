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
        if i['name'].upper() == item['name'].upper():  # upper !!!!!!!!!!!!!!
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
        if name == item['name'].upper():  # added .upper!!!!!!!!!!!
            item_found = True
            print(f'[INFO] Removing item {item}')
            remove_item(item)

    if not item_found:
        print(f'Sorry, we did not find {name} in inventory.')


def find_item_by_name(name):
    """Look up Item by NAME"""
    item_count = 0
    item_found = False
    for item in INVENTORY.copy():
        if name.upper().strip(' ') == item['name'].upper().strip(' '):
            item_found = True
            item_count += 1
            print(item)
    if not item_found:
        print(f'Sorry, did not find any {name} in inventory.')
    else:
        print(f'Found {item_count} of {name} in inventory. ')


def find_item_by_type(typ):
    """find item by TYPE"""
    item_count = 0
    item_found = False
    for item in INVENTORY.copy():
        if typ.upper().strip(' ') == item['type'].upper().strip(' '):
            item_found = True
            item_count += 1
            print(item)
    if not item_found:
        print(f'Sorry, did not find any {typ} in inventory. ')
    else:
        print(f'Found {item_count} of {typ} in inventory. ')


def find_by_price_grt(price):
    """find by price GREATER"""
    item_count = 0
    item_found = False
    for item in INVENTORY.copy():
        if price <= float(item['price']):
            item_found = True
            item_count += 1
            print(item)
    if not item_found:
        print(f'Sorry, did not find any item greater than {price:.2f}! ')
    else:
        print(f'Found {item_count} greater than {price:.2f}! ')


def find_by_price_lss(price):
    """find by price LESS"""
    item_count = 0
    item_found = False
    for item in INVENTORY.copy():
        if price >= (item['price']):
            item_found = True
            item_count += 1
            print(item)

    if not item_found:
        print(f'Sorry, did not find any item less than {price:.2f}! ')
    else:
        print(f'Found {item_count} less than {price:.2f}! ')
