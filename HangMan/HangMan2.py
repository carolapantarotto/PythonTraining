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
    if numberOfLives==5:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|_______")  
    if numberOfLives==4:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|    |")
        print("|    |")
        print("|")
        print("|")
        print("|_______") 
    if numberOfLives==3:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|   /|")
        print("|    |")
        print("|")
        print("|")
        print("|_______") 
    if numberOfLives==2:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|   /|\\")
        print("|    |")
        print("|")
        print("|")
        print("|_______") 
    if numberOfLives==1:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|   /|\\")
        print("|    |")
        print("|   / ")
        print("|")
        print("|_______") 
    if numberOfLives==0:
        print("_________")
        print("|/   | ")
        print("|   (_)")
        print("|   /|\\")
        print("|    |")
        print("|   / \\")
        print("|")
        print("|_______") 


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
    lives = 6
# BE: Choose the word
    secret_word = (random.choices(global_dictionary))[0]
    known_bool = [0]*len(secret_word)
    known_bool[0] = 1
    #Build known_word | known_word = "h _ _ _ _ _ _"
    known_word = coolDisplay(secret_word, known_bool)
# Loop
    while (lives>0):
        if (sum(known_bool)==len(secret_word)):
            print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
            print("You win! The word is: %s !" % (known_word))
            print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
            break
    # BE: Display word i.e. hangman: h _ _ _ _ _ _ 
        print ("You have %s lives left!" % (lives))
        hangmanGraphic(lives)
        print ("Guess the word: ", known_word)
    # User: Letter in input
        letter = input("Guess a letter: ")
    # BE: Check if the letter is part of the word
        save = False
        for i in range(1, len(secret_word), 1): #1 is included, len(secret_word) is excluded
            #print (secret_word[i])
            if (letter == secret_word[i]):
                # YES: Check if there is more than one occurrence in the word
                #       and update the known_bool
                known_bool[i] = 1
                save=True
        if (save==False):# NO: Remove one life
            lives-=1
        known_word = coolDisplay(secret_word, known_bool)
# End Loop
    if (sum(known_bool)!=len(secret_word)):
        hangmanGraphic(lives)
        print ("You lose!")
                
print ("Welcome to the Hangman game!")
start = "N"
while (start != "Y"):
    start = input("Do you want to play (Y/N)? ")
    if start=="Y":
        main()
        break