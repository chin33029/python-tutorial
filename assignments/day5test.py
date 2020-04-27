"""test"""

tries = 0

while tries < 5:
    WORD = input('Give me an adverb > ')
    tries += 1
    if WORD.endswith('ing'):
        print('Thanks.... I got my adverb')
        break
else:
    print('sorry youre out of tries')
