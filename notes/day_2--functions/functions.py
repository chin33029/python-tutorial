""" functions example """

# functions = action
# methods = just like function but it is dcefined in a class



# You can assign a default vaule for a argument and it will be used
# if the caller does not pass the argument
def say_hello(name='Stranger'):
    # username = '_'.join(name.lower())
    username = get_username(name)
    print(f'Hello {name}.  Your username is {username}')


# This handles the same logic as what we did in assignment one
def do_assignment_one(name, year):
    # say_hello(name)
    username = get_username(name)
    calculated_age = calculate_age(year)
    # print('Your age is ' + str(calculated_age))
    print(f'Hello {name} [ username={username}, age={calculated_age} ]')


def get_username(name):
    return '_'.join(name.lower())

def calculate_age(year):
    return 2020 - year

def main():
    """ My main entry point """
    say_hello()
    print(f'Another calculate age is {calculate_age(1982)}')  # this guy takes care of converting int to str
    # print('Another calculate age is ' + str(calculate_age(1982)))
    do_assignment_one('Dean', 1974)

# for name in ['Dean', 'Jason', 'Ricky', 'Samuel', 'Rahul']:
#     say_hello(name)

if __name__ == '__main__':
    main()
