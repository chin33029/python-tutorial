""" Inventory 2 """

VALID_TYPES = ['VODKA', 'TEQUILA']


def ask_for_type():
    """ ask for type """
    while True:
        liqour_type = input('What liqour type? ')
        if liqour_type.upper() in VALID_TYPES:
            return liqour_type.upper()
        print(f'{liqour_type} is not valid.  Try again.\n')


if __name__ == "__main__":
    STORE = []

    while True:
        if len(STORE) >= 2:
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
        PRICE = input('What price? ')
        PRICE = float(PRICE)
        ID = len(STORE)
        STORE.append({
            'id': ID,
            'name': NAME,
            'type': TYPE,
            'price': PRICE
        })

    print(f'\nYour inventory is: \n{STORE}')
