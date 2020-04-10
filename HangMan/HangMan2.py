# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:39:01 2020

@author: cpantarotto
"""
# Lib
import random
#import numpy
# DataSet of words
global_dictionary = ["outside","squirrel", "straight", 
              "finger", "leaf", "frog", "mouth", "grandson"]
MAX_LIVES = 6

def hangmanGraphic (numberOfLives):
    if numberOfLives==6:
        print("_________")
        print("|/   | ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_______")            
    elif numberOfLives==5:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_______")  
    elif numberOfLives==4:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|    |")
        print("|    |")
        print("|")
        print("|")
        print("|_______") 
    elif numberOfLives==3:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|   /|")
        print("|    |")
        print("|")
        print("|")
        print("|_______") 
    elif numberOfLives==2:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|   /|\\")
        print("|    |")
        print("|")
        print("|")
        print("|_______") 
    elif numberOfLives==1:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|   /|\\")
        print("|    |")
        print("|   / ")
        print("|")
        print("|_______") 
    elif numberOfLives==0:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|   /|\\")
        print("|    |")
        print("|   / \\")
        print("|")
        print("|_______") 

def guessPrint(lives, known_word, letter):
    # BE: Display word i.e. hangman: h _ _ _ _ _ _ 
        print ("You have %s lives left!" % (lives))
        hangmanGraphic(lives)
        print ("Guess the word: ", known_word)
    # User: Letter in input
        letter = input("Guess a letter: ")
        return letter

def printWinMessage(known_word):
    print("\n")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    print("You win! The word is: %s !" % (known_word))
    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
            
def coolDisplay(word, known_bool):
    cool_word = word[0]
    #Build known_word | known_word = "h _ _ _ _ _ _"
    for i in range (1, len(word), 1): #>1 as the first letter is already displayed
        if known_bool[i]==0:
            cool_word = cool_word + " _"
        elif known_bool[i]==1:
            cool_word = cool_word + " " + word[i]
    return cool_word

def main ():
# Start of the program
    lives = MAX_LIVES
    letter = ""
# BE: Choose the word
    secret_word = (random.choices(global_dictionary))[0]
    known_bool = [False]*len(secret_word)
    known_bool[0] = True
    #Build known_word | known_word = "h _ _ _ _ _ _"
    known_word = coolDisplay(secret_word, known_bool)
# Loop
    while (lives>0):
        if all(known_bool):
            printWinMessage(known_word)
            break
    # BE: Display word i.e. hangman: h _ _ _ _ _ _ 
        letter = guessPrint(lives, known_word, letter)
    # BE: Check if the letter is part of the word
        save = False
        for i in range(1, len(secret_word), 1): #1 is included, len(secret_word) is excluded
            #print (secret_word[i])
            if (letter == secret_word[i]):
                # YES: Check if there is more than one occurrence in the word
                #       and update the known_bool
                known_bool[i] = 1
                save=True
        if not save:# NO: Remove one life
            lives-=1
        known_word = coolDisplay(secret_word, known_bool)
# End Loop
    if not all(known_bool):
        hangmanGraphic(lives)
        print ("You lose!")
                
print ("Welcome to the Hangman game!")
start = ""
while (start != "N"):
    start = input("Do you want to play (Y/N)? ")
    if start=="Y":
        main()