""" Main """
from inventory import get_inventory, add_item, remove_item_by_name, find_item_by_name, find_item_by_type, find_by_price_grt, find_by_price_lss

if __name__ == "__main__":

    while True:
        USER_INPUT = input('What would you like to do' +
                           '(add/exit/delete/list/find)? ')
        USER_FORM = USER_INPUT.lower().strip(' ')
        if USER_FORM == 'exit':
            print('Goodbye!!!')
            break
        if USER_FORM == 'add':
            NAME = input('What is name of the item? ')
            NAME = NAME.upper().strip(' ')
            TYPE = input('What is item type? ')
            TYPE = TYPE.upper().strip(' ')
            PRICE = input('What is the price? ')
            add_item({'name': NAME, 'type': TYPE, 'price': PRICE})
            continue
        if USER_FORM == 'delete':
            DEL_ITEM = input(
                'What is the name of the Item you' +
                'wish to delete? ').upper().strip()
            remove_item_by_name(DEL_ITEM)
            continue
        if USER_FORM == 'list':
            print(get_inventory())
            continue

        while USER_FORM == 'find':
            FIND_OPT = input(
                'Would you like to find by ' +
                '(name/type/price/back)').lower().strip(' ')
            if FIND_OPT == 'name':
                FIND_NAME = input('What is the name of the item? ')
                find_item_by_name(FIND_NAME)
                continue
            if FIND_OPT == 'type':
                FIND_TYPE = input('What type of liqour or liqours? ')
                find_item_by_type(FIND_TYPE)
                continue
            if FIND_OPT == 'price':  # PRICE BLOCK
                PRICE_PNT = float(input('What is your price point?'))
                LESSGRT = input(
                    'Select (less/greater)').lower().strip(' ')
                if LESSGRT == 'greater':
                    find_by_price_grt(PRICE_PNT)
                    continue
                if LESSGRT == 'less':
                    find_by_price_lss(PRICE_PNT)
                    continue
            if FIND_OPT == 'back':
                break
            if FIND_OPT != 'name' or 'type' or 'price':
                print('Invalid find function! ')
                continue
        else:
            print('Invalid entry please try again. ')
            continue
