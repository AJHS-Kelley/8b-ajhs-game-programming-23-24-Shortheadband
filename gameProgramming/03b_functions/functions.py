# FUNCTION -- a named piece of code that can be reused easily
# FUNCTION SiGNATURE -- Syntax for creating a new function.
def exampleFunctionA(): # NO PARAMETERS
    count = 0
    num = int(input("How many times do you want to wish a happy birthday"))
    while count < num:
        print("Happy Birthday!\n")
        count += 1
                
def exampleFunctionB(num, count): # PARAMETERS
    while count < num:
        print("Happy Birthday!\n")
        count += 1

# IF A FUNCTION REQUIRES PARAMETERS, YOUR CODE WILL CRASH WITHOUT THEM!

# RUNNING A FUNCTION IS KNOWN AS CALLING THE FUNCTION!
#exampleFunctionA()
#exampleFunctionB(5,0)

def rollDice(numDice, sizeDice):
    numRolled = 0
    while numRolled < numDice:
            roll = random.radint(1, sizeDice)
            sum += roll
            print(f"Roll: {roll}\n")
            print(f"Sum: {sum}\n")
            numRolled += 1
        return sum

#rolldice(3,6)
#rolldice(1,20)

strentghPlayer = rollDice(3,6)
dexterityPlayer = rollDice(3,6)
wisdomPlayer = rollDice(3,6)

print

def genstats():
    playerstats = [
         0, #Str
         0, #Dex
         0, #Con
         0, #Int
         0, #Wis
         0  #Cha
    ]
    i = 0
    while i < len(playerstats):
        playerstats[i] = rollDice(3, 6) # strength
        i += 1

    print("playerStats")

genstats()