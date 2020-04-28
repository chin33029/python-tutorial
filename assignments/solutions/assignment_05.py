# Create a inventory with a max of 10 items
# Each item should have an id (0-9)
# Ask the user if they want to add a liqour or exit
# Eample Flow:
# What do you want to do (add / exit)? add
#   What brand? Stoli
#   What type? Vodka
#   How much is it? 12.34
# What do you want to do (add / exit)? add 
#   What brand? Titos
#   What type? Vodka
#   How much is it? 11.44
# What do you want to do (add / exit)? exit 
#
# Your inventory is:
# [{'id': 0, 'name': 'Stoli', 'type': 'Vodka', 'price': 12.34}, {'id': 1, 'name': 'Titos', 'type': 'Vodka', 'price': 11.44}]
#   What type? Vodka
#   How much is it? 12.34
#
# If you add all ten, you should print inventory and say warehouse is full

if __name__ == "__main__":
    STORE = []
    VALID_TYPES = ['VODKA', 'TEQUILA']
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
        NAME = input('What brand? ')
        TYPE = input('What type? ').upper()
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
