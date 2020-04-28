""" Inventory 2 """

VALID_TYPES = ['VODKA', 'TEQUILA']
MAX_ITEMS = 2


def is_float(string):
    """ Checks if string is a float """
    if string.replace('.', '', 1).isdigit():
        return True
    return False


def ask_for_type():
    """ ask for type """
    while True:
        liqour_type = input('What liqour type? ')
        if liqour_type.upper() in VALID_TYPES:
            return liqour_type.upper()
        print(f'{liqour_type} is not valid.  Try again.\n')


def ask_for_price():
    """ ask for price """
    while True:
        price = input('What price? ')
        if is_float(price):
            return float(price)
        print(f'{price} is not valid.  Try again.\n')


if __name__ == "__main__":
    STORE = []

    while True:
        if len(STORE) >= MAX_ITEMS:
            print('Warehouse is full !!!')
            break
        ACTION = input('What do you want to do (add / exit)? ')
        if ACTION.lower() == 'exit':
            break
        if ACTION.lower() != 'add':
            print(f'{ACTION} is not a valid command.\n')
            continue
        TYPE = ask_for_type()
        NAME = input('What brand? ')
        PRICE = ask_for_price()
        ID = len(STORE)
        STORE.append({
            'id': ID,
            'name': NAME,
            'type': TYPE,
            'price': PRICE
        })  # [{id: 0, SDFasdfasdv}, {'this': 'that'}]
        STORE.append('something')
        STORE.append(12)
        STORE.append(13)

    print(f'\nYour inventory is: \n{STORE}')

    first_item = STORE[0]
    first_item['price'] = 1000000.12
    first_item['qty'] = 4
    print(first_item)

