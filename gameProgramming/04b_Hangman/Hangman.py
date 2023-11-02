# Hangman Game by Gabriel Coffey, vo.2

import random

words = 'Cat Bat Rat Car Bar Star Bored Help Belt Tilt Machine Hammer Hourglass Vogage Punishment Divine Rewind Combine TombStone Chrome Celestial Beatiful Guardian Alliance Lyric circular motherboard Critical Mystical Dynasty'.split()
print(words)
HANGMAN_BOARD = ['''
   
    +---+
        |         
        |         
        |         
     ========''', '''            
              
                 
    +---+
    0   |         
        |         
        |         
     ========''', '''            

    +---+
    0   |         
    |   |         
        |         
     ========''', '''            


    +---+
    0   |         
   /|   |         
        |         
     ========''', '''            


    +---+
    0   |         
   /|\  |         
        |         
     ========''', '''            


    +---+
    0   |         
   /|\  |         
   /    |         
     ========''', '''            

    +---+
    0   |         
   /|\  |         
   / \  |         
     ========''']

#i = 0
#while i < len(HANGMANBOARD):
#    print(HANGMAN_BOARD[I])
#    i += 1

# Pick Word from List
def getRandomWord(wordList): # Return a random word from the list
    wordIndex = random.randint(0,len(words) - 1)
    # len(listName) - 1 is EXTREMELY COMMON FOR WORKING WITH LISTS.
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters , secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])

#i = 0
#while i < 50:
#    word = getRandomWord(words)
#    print(word)
#    i += 1

