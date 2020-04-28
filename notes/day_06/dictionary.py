INVENTORY = [
    {'id': 0, 'name': 'Stoli', 'type': 'VODKA', 'price': 123.07},
    {'id': 0, 'name': 'Patron', 'type': 'TEQUILA', 'price': 124.97},
    {'id': 0, 'name': 'Titos', 'type': 'VODKA', 'price': 13.07}
]

name = input('What item do you want me to look up? ')

for item in INVENTORY:
    if name.lower() == item['name'].lower():
        print(f"Found your item and it costs {item['price']}")
        print(item)
        break
else:
    print(f'Sorry, could not find {name}')

liqour_type = input('What type do you want me to look up? ')

found_one = 0
for item in INVENTORY:
    if liqour_type.lower() == item['type'].lower():
        print(item)
        found_one += 1

if not found_one:
    print(f'Could not find any {liqour_type}')
else:
    print(f'Found {found_one} items of type {liqour_type}')
