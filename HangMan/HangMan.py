# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:39:01 2020

@author: cpantarotto
"""
def main ():
# Start of the program
    lives = 6
# BE: Choose the word
    secret_word = "hangman"
    word_l = len(secret_word)
    known_word = secret_word[0]
    #Build known_word | known_word = "h _ _ _ _ _ _"
    i = word_l
    while (i>1): #>1 as the first letter is already displayed
        known_word = known_word + " _"
        i-=1
# Loop
    while (lives>0):
    # BE: Display word i.e. hangman: h _ _ _ _ _ _ 
        print ("You have %s lives left!" % (lives))
        print ("Guess the word: ", known_word)
    # User: Letter in input
        letter = input("Guess a letter: ")
    # BE: Check if the letter is part of the word
        array_known_word = list(known_word)
        save = False
        for i in range(1, word_l, 1): #1 is included, word_l is excluded
            #print (secret_word[i])
            if (letter == secret_word[i]):
                # YES: Check if there is more than one occurrence in the word
                #       and update the known_word
                array_known_word[2*i] = letter
                save=True
        if (save==False):# NO: Remove one life
            lives-=1
        known_word = ''.join(array_known_word)
# End Loop
                
print ("Welcome to the Hangman game!")
start = "N"
while (start != "Y"):
    start = input("Do you want to play (Y/N)? ")
    if start=="Y":
        main()
        break