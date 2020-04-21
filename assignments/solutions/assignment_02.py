""" Assignment 02 - Bank Example """


def deposit(amount, balance):
    """ Deposit money to account """
    return int(balance) + int(amount)


def withdraw(amount, balance):
    """ Withdraw money from account """
    if int(amount) > int(balance):
        print(f'Unable to withdraw {amount}, you only have {balance}')
        return balance
    else:
        return int(balance) - int(amount)


if __name__ == "__main__":
    # Set the beginning balance
    BALANCE = 100

    # Welcome the customer
    print('\nWelcome to First Python Bank.')

    # Tell the user their current balance
    print(f'Your current balance is {BALANCE}\n')

    # Ask the customer what action do they want to take.
    # Uppercase the response too make it easier for comparisons
    ACTION = input(
        'What would you like to do (Deposit / Withdraw / Exit)? '
        ).upper()

    # Keep processing until the user wants to exit
    while ACTION != "EXIT":

        # Check if the user entered a valid action
        if ACTION in ('DEPOSIT', 'WITHDRAW'):

            # Ask the user how much
            AMOUNT = input('How much? ')

            # Process the transaction
            if ACTION.upper() == 'WITHDRAW':
                BALANCE = withdraw(AMOUNT, BALANCE)
            else:
                BALANCE = deposit(AMOUNT, BALANCE)

            # Tell the user their new balance
            print(f'Your balance is now {BALANCE}\n')

        # Tell the user that the entered actionis not valid
        else:
            print(f'Sorry, {ACTION} is an invalid action.\n')

        # Ask the user what they want to do next
        ACTION = input(
            'What would you like to do (Withdraw / Deposit / Exit)? '
            ).upper()

    # Tell the user what their final balance is
    print(f'Your final balance is {BALANCE}.')

    # Thank the user for being a customer
    print('Thank you for being a First Python Bank customer.')
