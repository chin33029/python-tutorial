# variables
# var = 1
# var = 'string'
# var = 1.0
# var = [0,1,2,3]

# dictionary 
# var = {
#    "name": "Dean",
#    "phone": "123-456-7890"
# }

# dictionary consists of key/value pairs
# { 
#   key1: value1,
#   key2: value2
# }

# person = {
#     'firstName': 'Dean',
#     'lastName': 'Chin',
#     'phone': '123-456-7890'
# }

# print(person['lastName'] + ', ' + person['firstName'])


# liquor = {
#     'name': input('What brand? '),
#     'type': 'Vodka',
#     'price': 100.09
# }

# print(liquor)
# liquor['name'] = input('What brand? ')
# print(liquor)
# liquor['qty'] = int(input('How much? '))
# print(liquor)

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

store = []
store.append({
    'name': input('What brand? '),
    'type': input('What type? '),
    'price': float(input('What price? '))
})
store.append({
    'name': input('What brand? '),
    'type': input('What type? '),
    'price': float(input('What price? '))
})

print(store)
