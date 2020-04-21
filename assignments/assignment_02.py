"""Bank Assignment"""


BEGINING = 100


def say_hello(BEGINING):
    print('Welcome To First Python Bank')
    print(f'Your Current Balance Is {BEGINING}')
      

def dep(dep_amt, BEGINING,):
    return int(dep_amt) + BEGINING
       

def withdraw(with_amt, BEGINING):
    if int(with_amt) < int(BEGINING):
       return BEGINING - int(with_amt) 
    else: 
       print(f'Unable to withdraw {with_amt}, you only have {BEGINING}')
    return BEGINING





if __name__ == '__main__':

    say_hello(BEGINING)
customer_option = input('What would you like to do(Deposit, Withdraw, Exit)?')
customer_input = customer_option.lower().strip('')
chk_val = 0

if customer_input == 'deposit':
    dep_amt = input('How much would you like to deposit?')
    chk_val = int(chk_val) + 1
    print('Your Balance is Now ' + str(dep(dep_amt, BEGINING)))
           
if customer_input == 'withdraw':
    with_amt = input('How much would you like to withdraw?')
    chk_val = int(chk_val) + 1 
    print('Your Balance is Now ' + str(withdraw(with_amt, BEGINING)))

if customer_input == 'exit':
    chk_val = int(chk_val) + 1
    print(f'Your Balance is {BEGINING} ')
    print('Have a Nice Day!')
if chk_val == 0:
    print(f'Sorry, {customer_option} is an invalid action.')
    
