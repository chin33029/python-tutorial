""" This is my first application """
# print('Dean')

# print('Hello Dean')

# name = "Jason"  # Variable example

# print('Hello ' + name)  # String Concatenation
# print('Hello ' + name)
# print('Hello ' + name)
# print('Hello ' + name)
# print('Hello ' + name)

# print(1 + 2)  # Adding integers
# print(1.2 + 1.3)  # Adding floats
# print(1 + 1.2)

# print('1' + '2')  # Adding strings

# print('1' + '2')  # Adding string + integer

# IF name = "Dean" then print Dean Sucks
# else print <name> is cool

# name = " DeAn "  # Variable example
# name_formatted = name.upper().strip(' ')
# if name_formatted == "DEAN":
#     print(name_formatted + ' Sucks')
# else:
#     print(name_formatted + ' is cool')


# name="Dean"
# # if Ricky = Cool
# # if Samuel = Cooler
# # if Rahul = the best
# # else = mkay
# if name == 'Ricky':    # boolean: True or False
#     print(name + ' = Cool')
# elif name == 'Samuel':
#     print(name + ' = Cooler')
# elif name == 'Rahul':
#     print(name + ' = the best')
# else:
#     print(name + ' = mkay')

name="Dean" # ['D','e','a','n']

# a = str(1)
# b = str(2)
# print(a + b)

# for i in range(0,5):  # for i in [0,1,2,3,4] <--array
#     print(str(i) + ' - ' + name)  # str(1)

# for i in name:  # for i in [D,e,a,n] <--array
#     print(str(i) + ' - ' + name)  # str(1)

for i in range(0,5):  # for i in [0,1,2,3,4] <--array
    print('---- i = ' + str(i) + '---------')
    print(i * 5)  # str(1)
    print(i * 2)



# Types: array, float, string, integer, boolean
# Functions: for loop, if, elif, else, print, str, concatenation, range
#       upper, lower, strip, lstrip, rstrip
# variables


# if name is Dean then
# how many shot in a bottle
# each shot = 2 oz
# oz in a bottle 32 oz

total_sum = 0
total_shots = 0
shot_oz = 6
while total_sum + shot_oz < 32:
    total_sum = total_sum + shot_oz
    total_shots = total_shots + 1

print('total shots = ' + str(total_shots))
print('total sum = ' + str(total_sum))

