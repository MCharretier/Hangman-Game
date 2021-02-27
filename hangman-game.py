#MODULES:
from data import *
from functions import *


#VARIABLES:
score = recupScore ()
utilisator = recupUtilisator ()
keepPlaying = str()


#PROGRAM:
if utilisator not in score.keys():
    score[utilisator] = 0
    print (f"Welcome {utilisator}, good luck !")
    print ("...")
else:
    print (f"Good luck {utilisator} !")
    print ("...")

while keepPlaying != "n":
    
    lastTries = nbTries
    findLetters = []
    loseLetters = []
    hiddenWord = str ()
    wordToFind = randomWord ()
    
    
    while hiddenWord != wordToFind and lastTries > 0:
        
        letter = recupLetter ()
        
        if letter in findLetters:
            print ("Letter already entered... Start over:")
            print ("...")
    
        elif letter in loseLetters:
            print ("Letter already entered... Start over:")
            print ("...")
            
        elif letter in wordToFind:
            findLetters.append (letter)
            print (f"Well done, you found the letter: {letter} !")
            print ("...")
        
        else:
            loseLetters.append(letter)
            lastTries -= 1
            print (f"Missed... the word does not contain: {letter} ...")
            print (f"You still have {lastTries} chances.")
            print ("...")
            
        hiddenWord = recupHiddenWord (wordToFind , findLetters)
        print (f"{hiddenWord}")
        
        
    if hiddenWord == wordToFind:
        score[utilisator] += lastTries
        print (f"Congratulations, you found the word: {wordToFind} !")
        print (f"You earn {lastTries} points !")
        print (f"Your score is now: {score[utilisator]} points.")
        print ("...")
    else:
        print (f'Hanged ! The word was "{wordToFind}"')
        print (f"Your score remains: {score[utilisator]}")
        print ("...")
        
        
    keepPlaying = str (input ("Do you want to continue ? (y/n)"))
    keepPlaying = keepPlaying.lower ()
    
saveScore (score)
os.system("pause")