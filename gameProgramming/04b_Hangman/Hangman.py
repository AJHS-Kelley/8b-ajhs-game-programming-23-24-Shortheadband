# Hangman Game by Gabriel Coffey, v0.4
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
    print()

    print('Missed Letters:', end = '')
    for eachLetter in missedLetters:
        print(eachLetter, end = '')
    print()
    blanks = '_' * len(secretWord)

    # Replace Blanks with Correct Letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = '')
    print()    


def getGuess(alreadyGuessed):
    while True:
        print('Please guess a letter amd press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('Letter has been guessed already, try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please guess a LETTER from the English alphabet.')
        else:
            return guess
            
    def playAgain():
        print('Do you want to play again? Yes or No?')
        return input().lower().startswith('y')
        
    # Introduce the game
    print('Welcome to Hangman by Ryan K.')
    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord(words)
    gameIsDone = false
    
    # Main Game Loop
    while True:
        displayBoard(missedLetters, correctLetters, secretWord)
        
        guess = getGuess(missedLetters + correctLetters)
        
        if guess in secretWord:
            correctLetters = correctLetters + guess
            
            # Check To See If Winner, Winner Chicken Dinner
            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = false
                    break
                if foundAllLetters:
                    print('That is pretty based! well Done.')
                    print('The secret word was' + secretWord)
                    gameIsDone = True
        else:
            missedLetters = missedLetters + guess
            
            if len(missedLetters) == len(HANGMAN_BOARD) - 1:
                displayBoard(missedLetters, correctLetters, secretWord)
                print('You have run out of huesses and lost the game.')
                print('you made this number of correct guesses' + str(len(correctLetters)))
                print('The secret word was ' + secretWord)
                gameIsDone = True
                
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
                

#i = 0
#while i < 50:
#    word = getRandomWord(words)
#    print(word)
#    i += 1

