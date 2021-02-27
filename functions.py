#MODULES:
import pickle
import os
from random import choice
from data import *

#FUNCTIONS:

def recupScore ():
    if os.path.exists ("saves.txt"):
        with open("saves.txt","rb") as saves:
            oldScoreUnpickler = pickle.Unpickler (saves)
            score = oldScoreUnpickler.load()
    else:
        open("saves.txt" , "a").close()
        score = {}
    return score


def saveScore (score):
    with open("saves.txt" , "wb") as saves:
        newScore = pickle.Pickler (saves)
        newScore.dump (score)
 
 
def recupUtilisator ():   
    nomUtilisator = str (input ("What's your name ?"))
    nomUtilisator = nomUtilisator.capitalize() 
    if not nomUtilisator.isalnum():
        print ("Invalid name !")
        return recupUtilisator()
    else:
        return nomUtilisator


def randomWord ():
    wordToFind = choice(liWords)
    return wordToFind


def recupLetter (): 
    letter = str (input ("Submit a letter:"))
    letter = letter.lower()  
    if len(letter) > 1 or not letter.isalpha():
        print ("Invalid enter !")
        return recupLetter()
    else:
        return letter
    
    
def recupHiddenWord (wordToFind , findLetters):  
    hiddenWord = str () 
    for letter in wordToFind:
        if letter in findLetters:
            hiddenWord += letter
        else:
            hiddenWord += "*"
    return hiddenWord