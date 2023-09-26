# Select the secret number from a given range.
# Player must guess the number.
# Compare guess to the secret number
# What happens if the guess is wrong?
    # Tell them the guess is wrong.
    # Tell them the number of guesses left.
    # Tell them if too high / too low.
# What happens if the guess is right?
    # Tell them guess is correct.
    # Award a point.
# What happens if the player runs out of guesses?
    # Tell player rounds has been lost.
    # Award point to CPU.
# Check to see if player or cpu has >= 3 points, if so they win.

import random # Import the random module to our code.

# DECLARATIONS
secretNumber = -1
playerGuess = int(-1)
playerScore = 0
cpuScore = 0
numberGuesses = 0
playerName = ""
difficulty = ""
rangeMin = ""
rangeMax = ""
numAttempts = ""
range,

print('"Guess The Number"')

playerName = input('What should I call you?\nType your name and press enter.\n')
# Verify Input Whenever Possible!
print(f'you want me to call you {playerName}. Is that correct?')
isCorrect = input("Please type yes if correct, no if not correct.\n")
if isCorrect == "yes":
    print(f"Ok {playerName}, let's continue")

rangeMin = int(input("Now let's set your difficulty.\n Please type the minuium range NUMBER and press enter.\n"))
if rangeMin == rangeMin:
    print(f"Ok {playerName}, let's continue")

rangeMax = int(input("Now Type the maxium range NUMBER and press enter.\n"))
if rangeMax == rangeMax:
    print(f"Ok {playerName}, let's continue")

numAttempts = int(input("Now type the NUMBER of attempts and press enter.\n"))
if numAttempts == numAttempts:
    print(f"Ok {playerName}, let's continue")

isDifficultyCorrect = input("Please type yes if correct, no if not correct.\n")
if isDifficultyCorrect == "yes":
    print(f"Ok {playerName}, let's continue")


# GAME LOOP
print("You need to guess a number from 0 to 20 and you have four guesses.\nIf you guess it right and you get a point.\nIf you guess wrong 5 times cpu gets a point")
# ADD CODE HERE TO CHANGE DIFFICULTY BETWEEN EACH MATCH
# print() an explanation of your your three difficulty levels
# Use input() to store diffculty in diffculty variables.
# assign values to numAttempts, rangeMin, and rangeMax based on choice

while playerScore != 3 and cpuScore != 3: # Start the match
    # pass -- Tells python to skip this block of code
    
    # CPU SECRET NUMBER GENERATION
    secretNumber = random.randint(rangeMin, rangeMax)
    
    # print(secretNumber)
    print(f"Player Score: {playerScore}\nCPU Score: {cpuScore}.\n")
    numberGuesses = 0



    for guesses in range(numAttempts):
        print(f"You have {5 - numberGuesses} guesses remaining.\n")
        playerGuess = input("Type a number from 0 to 20 and press ENTER.\n")
        
        # input() saves all data as a string by default.
        # int() will convert to an INTEGER
        # folat() will covert to a float
        print(f"You have chosen {playerGuess}. Let's see if you're right!\n")
        if playerGuess == secretNumber:
            print("Whoa dude, what a guess! You got in!\n")
            playerScore += 1
            break # IMMEDIATELY EXIT ANY LOOP YOU ARE IN!
        else:
            print("You did not guess correctly.\n")
            if int(playerGuess) > secretNumber:
                print("Your guess is too high.\n")
            else:
                print("Your guess is too low.\n")
        numberGuesses += 1
    if playerGuess != secretNumber:
        cpuScore != 1
        print("The Cpu wins a point since you ran out of guessess.\n")

if playerScore >= 3:
    print("Winner, winner, chicken dinner! You scored 3 points first!")
else:
    print("Bruh Imagine losing couldn't be me like on god")
