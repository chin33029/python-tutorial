# Assignment 6 - Bar Application

## Objective

Create a bar application that will allow a bar manager to do the following inventory operations:

* List inventory
* Add item to inventory
* Delete an item from inventory

## Special Instructions

* Create a new directory `assignments/assignment_06/`
* Copy the files from `notes/day_07` folder to the new `assignments/assignment_06/` folder
* Update the `assignments/assignment_06/bar.py` file to satisfy the requirements for the assignment.
* Look at previous assignment on how we utilized the while loops to keep asking a user for what action they would like to perform.

## Example Application Output

``` bash
Welcome to the Python Bar Inventory Application.

What action would you like to perform (list/add/delete/exit)? list

Inventory:
[{'name': 'Stoli', 'type': 'VODKA', 'price': 123.07}, {'name': 'Patron', 'type': 'TEQUILA', 'price': 124.97}, {'name': 'Titos', 'type': 'VODKA', 'price': 13.07}]

What action would you like to perform (list/add/delete/exit)? add

What is the name of the item? Absolute
What is the item type? VODKA
What is the price? 11.27

Added item {'name': 'Absolute', 'type': 'VODKA', 'price': 11.27}

What action would you like to perform (list/add/delete/exit)? list
[{'name': 'Stoli', 'type': 'VODKA', 'price': 123.07}, {'name': 'Patron', 'type': 'TEQUILA', 'price': 124.97}, {'name': 'Titos', 'type': 'VODKA', 'price': 13.07},{'name': 'Absolute', 'type': 'VODKA', 'price': 11.27}]

What action would you like to perform (list/add/delete/exit)? delete

What is the name of the item to delete? Titos

Deleted item {'name': 'Titos', 'type': 'VODKA', 'price': 13.07}

What action would you like to perform (list/add/delete/exit)? list

Inventory:
[{'name': 'Stoli', 'type': 'VODKA', 'price': 123.07}, {'name': 'Patron', 'type': 'TEQUILA', 'price': 124.97}, {'name': 'Absolute', 'type': 'VODKA', 'price': 11.27}]

What action would you like to perform (list/add/delete/exit)? exit

Goodbye!!!
```

## Extra Credit

* Make sure that the type is stored in the inventory in all upper case
