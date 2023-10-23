# Data Types and Operators, Ryan Kelley
# Variables Rules
# CANNOT START WITH A NUMBER
# CANNOT USE BULIT-IN KEYWORDS AS VARIABLES
# VARIABLES NAME SHOULD DESCRIBE THE DATA BEING STORED
# snake_case variables use _ to seperate words, all lowercase
# camelCase

# String Literal Examples
playerName = "Based"
emptyString = ""
spaceString = " "
storageName = "Big Box"

# Integer Data Types
health = 100
extralives = 5
temperature = -17
skillmeter = 10

# Floating Point Data Types
pi = 3.1415678
laptime = 3.5
velocity = -2.0
speed = 12.5

# Boolean Data Types
isFireType = False
weaponEquipped = True
pvpEnabled = False
pveEnabled = True

# Arithmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print(3 + 2) # Addition
print(30 - 25) # Subtraction
print(5 * 6) # Multiplication
print(3 / 1) # Division
print(3 ** 4) # Exponents
print(18 % 3) # Modulus -- divdes the 2 numbers and gives you the remainder, most commonly used to determine even/odd

# Comparison Operators
# Evaluate the expression, then return True or False
print (5 > 3) # Greater Than
print (7 >= -1) # Greater Than or Equal to
print (-1 < -2) # Less Than
print (0 <= 0) # Less Than or Equal to
print (5 == 3) # Is Equal to
print (-99 != 99) # Not Equal to

# Assignment Operators
myVariable = "myValue" # Assign variable on left tha value on the right, throw out any current value
myOtherVariable = (10 + 5)

myVariableAgain = 1
myVariableAgain = 5
print(myVariableAgain)

# Addition Assignment -- add the value on the right, keeping any current value
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x = 0
x += 1
x = x + 1

# Logical Operators
print(3 > 5 and 4 < 3) # and requires All expressions to be true
print(3 > 2 and 4 < 3)
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 != 3 and favColor == "Blue" and temp == -5)
# When Writing and expressions, put the value most likely to be False first!

# Logical OR -- Requires One expression to be true
print(5 > 2 or 2 < -2)
print(3 != 3 or 5 == 5)

# AND OR Combined
print("Line 81")
print(3 > 2 or 4 < 3 and 5 != 7 )
# print(True and False and True)
# Not Logical Operator, 
print(not(3 > 2)),
print(not)not)not)5 !=3))))