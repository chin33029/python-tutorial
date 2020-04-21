# create a function to say hello, <name>
# call the function to say hello and pass dean as name

# create a function called add_five(number)

# create a function called mixed_case_name(first, last)
# So that it will print 'DEAN chin' if I pass mixed_case_name('dean', 'Chin')

def hello(name):
    print(f'hello {name}')


def add_five(number):
    number -= 5
    print(number)

def mixed_case_name(first, last):
    print(f'{first.upper()} {last.lower()}')

# mixed_case_name('dean', 'Chin')
# mixed_case_name('Samuel', 'urSO')
# add_five(5)

def lookup_age(first, last):
    if first.lower() == 'samuel':
        return 12
    if first.lower() == 'ricky':
        return 25


# def should_i_sell_him_a_gun(first, last):

#     result = True
#     # check if under age
#     if lookup_age(first, last) < 21:
#         # return False
#         result = False

#     # don't allow if they have a record
#     if has_a_criminal_record(first, last):
#         return False

#     # dont let them buy if they recently bought a gun    
#     if purchased_a_gun_within_24_hours(first, last):
#         return False

#     # if i reached here, then all is good
#     return True

# def is_a_minor(first, last):
#     if lookup_age(first, last) < 13:
#         return True
#     else:
#         return False

# result = should_i_sell_him_a_gun(first, last)
def add_digits(first_num, second_num):
    return first_num + second_num

sum = add_digits(1, 2)

def func1():
    sum = 0
    
    if False:
        # print('One')
        sum += 1
    if False:
        # print('Two')
        sum += 2
    if True:
        # print('Three')
        sum += 3
    if True:
        # print('Four')
        sum += 4
    if True:
        # print('Five')
        sum += 5

    return sum

result = func1()  # result = 1
print(f'result={result}')




