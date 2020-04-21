
magic_number = 7
tries = 0

max_tries = 3
while tries < max_tries:
    # if int(input('Guess > ')) == magic_number:
    # line above is the same as the two below    
    guess = input('Guess > ')
    if int(guess) == magic_number:
        print('You won $$$$$$')
        break
    tries += 1
else:
    print(f'You lost.  You had {max_tries} tries')

print('End Game')