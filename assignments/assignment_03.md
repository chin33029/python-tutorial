# Assignment 3

## Scenario

For this assignment we will simulate a bar where at the beginning it will have one bottle of alcohol that has a max of 32 shots.

As part of this exercise, you will start of with a full bottle that has 32 shots in it.  You will need to ask the customer how many shots they want and subtract it from the total.  Once you are out of shots in the bottle, you should inform the customer that the bottle is now out of stock.

```bash
# Example output for normal sales until we run out of shots
Welcome to Python Bar.
We have 32 shot(s) for sale

How many shots do you want (type exit to leave)? 30
Sold 30 shot(s) [2 shot(s) left

How many shots do you want (type exit to leave)? 3
Not enough in bottle for 3 shot(s) [2 shots left]

How many shots do you want (type exit to leave)? 2
Sold 2 shot(s) [0 shot(s) left

Closing up the bar because we have no more shots left.
Thank you for being a Python Bar customer.

# Example output if customer leaves before finishing all shots
Welcome to Python Bar.
We have 32 shot(s) for sale

How many shots do you want (type exit to leave)? 10
Sold 10 shot(s) [22 shot(s) left

How many shots do you want (type exit to leave)? exit
Thank you for being a Python Bar customer.
```

## Additional Details

Try and do this assignment without looking at the previous assignment 2 solution.  If you really get stuck, then use the assignment 2 solution as a guide.

The solution should have at least one function.

## Extra Credit

Add a check if the amount is not an integer and inform the customer that they have to enter a integer or 'exit'.  You can google and see what the python command is to see if a string is a digit.

```bash
# Example output for an invalid input
Welcome to Python Bar.
We have 32 shot(s) for sale

How many shots do you want (type exit to leave)? asdf
Please enter an integer or 'exit'

How many shots do you want (type exit to leave)? 4
Sold 4 shot(s) [28 shot(s) left

How many shots do you want (type exit to leave)? exit
Thank you for being a Python Bar customer.
```
