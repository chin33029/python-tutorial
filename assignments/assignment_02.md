# Assignment 02 - First Python Bank

## Scenario

For this assignment, we will simulate a ATM machine.
You will need to write a program to satisfy the following scenario:

* The user should have an initial balance of 100
* Ask the user if they want to ddeposit or withdraw
* Tell the user their new balance

```bash
# Example output for a deposit
Welcome to First Python Bank.
Your current balance is 100

What would you like to do (Deposit / Withdraw / Exit)? deposit
How much? 15
Your balance is now 115

# Example output for a withdraw
Welcome to First Python Bank.
Your current balance is 100

What would you like to do (Deposit / Withdraw / Exit)? deposit
How much? 35
Your balance is now 65

# Example output for a withdraw that is more than the balance
Welcome to First Python Bank.
Your current balance is 100

What would you like to do (Deposit / Withdraw / Exit)? withdraw
How much? 110
Unable to withdraw 110, you only have 100
Your balance is now 100

# Example output for a withdraw that is more than the balance
What would you like to do (Withdraw / Deposit / Exit)? blah
Sorry, BLAH is an invalid action.
```

## Additional Details

I created a `assignements\assignment_02.py` file in this repo that you can use as a starting point.  It contains a couple functions that you will need to fill in the logic for and also the logic for the main section.

The program should allow the action entered to be case insensitive.  Example, the user can enter deposit or Deposit or DEPOSIT and the program will treat them all as a deposit.

## Hints

* The functions should return the new balance

## Extra Credit

Update the program to utilize a while loop that will keep asking the user what type of action they want to perform until they enter exit.  This one is meant to be a little difficult.  Give it a shot and we can discuss in the next meeting on the solution.

```bash
# Example of extra credit
Welcome to First Python Bank.
Your current balance is 100

What would you like to do (Deposit / Withdraw / Exit)? withdraw
How much? 50
Your balance is now 50

What would you like to do (Withdraw / Deposit / Exit)? deposit
How much? 20
Your balance is now 70

What would you like to do (Withdraw / Deposit / Exit)? exit
Your final balance is 70.
Thank you for being a First Python Bank customer.
```
