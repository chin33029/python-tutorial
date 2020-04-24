
# magic_number = 7
# tries = 0

# max_tries = 3
# while tries < max_tries:
#     # if int(input('Guess > ')) == magic_number:
#     # line above is the same as the two below    
#     guess = input('Guess > ')
#     if int(guess) == magic_number:
#         print('You won $$$$$$')
#         break
#     tries += 1
# else:
#     print(f'You lost.  You had {max_tries} tries')

# print('End Game')


# If I need to do something multiple times:
#   for or a while loop
# If I need to do a comparison
#   use if / elif / else
# If I need to check more than one thing if it is true
#   use `or`.  This will evaluate true for any comparison that evaluates to True
#   if string == "something" or string == "somethingelse":
#       will come into this block if any of the above is True
#   elif string == "anotherthing":
#       will come into this block if elif evaluates to True
#   else:
#       gets in here if the if statement is false and if the elif statement is false.
# The while, else gives you the ability to execute a line of code if the while condition exhausts all its tries
# while try < max_tries:
#   if condition:
#      do something
#      break
# else:
#   reached max_tries
#
# You can also write this with a for loop
# for i in range(0,5):
#   if condition:
#      do something
#      break




# for i in 'deano': # This is the same 
#     print(f'you are at {i}')
#     word = input('Give me an adverb')
#     if word.endswith('ing'):
#         print('You got it')
#         break
# else:
#     print('Sorry, you reached the max tries')

string = 'deano' # ['d', 'e', ...]
i = 0
str_length = len(string)
while i < str_length:
    print(string[i])
    i += 1

print('\n')
for c in 'deano':
    print(c)

