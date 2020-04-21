# 750 ml
# 500 ml

# All bottles are liter (32 oz)
# shot is 2 oz


# margarita
# - tequila
# - triple sec

# cosmo:
# - vodka
# - triple sec

# manhattan:
# - whiskey
# - sweet vermouth

TEQUILA_REMAINING_OZ = 32
VODKA_REMAINING_OZ = 32
TRIPLE_SEC_REMAINING_OZ = 32
SHOT_SIZE = 2


def pour_drink(type_of_drink, size_before_pour):
    """ Pour a drink """
    print(f'Puring a {type_of_drink}')
    # return f'Returning with {type_of_drink}'
    return size_before_pour - SHOT_SIZE

# Ask the user what type of drink do they want.
# pour the alcohol required for the drinks
# give the inventory of what is left.
# User can say clos and it will exit


DRINK_TYPE = input('What type of drink do you want? ')
print(DRINK_TYPE) # soda
# result = pour_drink(DRINK_TYPE) # Puring a soda
# print(result) # Returning with soda
# print(pour_drink(DRINK_TYPE)) # Puring a soda \n Returning a soda
# print(result) # Returning with soda
print(f'You have {pour_drink(DRINK_TYPE, 25)} left in bottle')





