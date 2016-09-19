

import random

print("welcome to hangman! you have 8 attempts, before you are done!")
with open("/usr/share/dict/words") as word_file:

    word_file = word_file.readlines()
    unpredictability = random.choice(word_file)
    hang_man = "'_'" * len(unpredictability)

    print(hang_man)
    print(len(unpredictability))
    print("characters in your word")

    attempts = input("please enter your guess")
    gaps = "_" * len(unpredictability)
    attempts = 8
    '''if attempt is'''
    '''while attempts =< 8 len(unpredictability)'''
    print(unpredictability)
