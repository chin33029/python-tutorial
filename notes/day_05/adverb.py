# ask user for a word
# if it ends with ing, then say this is probably an adverb
# else, I don't know what that is.

# Keep asking the user to type an adverb until they finally type one.
# Give me an adverb > dodo
# Give me an adverb > dodoing
# Thanks.... I got my adverb


# WORD = input('Gimme a word > ')
# while WORD.endswith():

#       if WORD.endswith('dodo'):
#         print('This is a probably an adverb')
#     if Word.endswith('dodoing'):
#             print ('This is an adverb')
#         break

#     print('Thanks... i got my adverb')


# Give me an adverb > dodo
# Give me an adverb > dodoa
# Give me an adverb > dodo
# Give me an adverb > dodo
# Give me an adverb > dodo
# Sorry, no more tries.  You have already tried 5 times

# Give me an adverb > dodo
# Give me an adverb > dodo
# Give me an adverb > dodoing
# Thanks.... I got my adverb
tries = 0
max_tries = 5
while tries < max_tries:
    WORD = input('Give me an adverb > ')
    tries += 1
    if WORD.endswith('ing') or WORD.endswith('ed'):
        print('Thanks.... I got my adverb')
        break

else:
    print(' Sorry no more tries ')
