"""
Create a python file called assignment_1.py
Write a program that will do the follow:
  - Prompt the user for their first name
      We have not learned this yet so here is the syntax
      name = input('What is your first name? ')
  - Prompt the user for the year that they were born
      We have not learned this yet so here is the syntax
      year = input('What year were you born? ')
  - From the name that you received from the input, we will figure out a username.
      username should be all lowercase and characters seperated by underscores.
  - From the year that was given, you will need to figure out their age

Program output should look similar to this.
What is your first name? Dean
What year were you born? 1974
Hello Dean
Your username is d_e_a_n
You are 46 years old
"""

# Get information about the user
name = 'Rahul'
year = input('What year were you born? ')

# Determine the user's name
username = ""
for char in name.lower():
    username = username + char + '_'
username = username.strip('_')

# Determine the user's age
age = 2020 - int(year)

# Print out information about the user
print('Hello ' + name)
print('Your username is ' + username)
print('You are ' + str(age) + ' years old')