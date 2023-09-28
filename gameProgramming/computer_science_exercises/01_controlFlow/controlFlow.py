# Control Flow, Gabriel Coffey, v0.0
# DECLARATIONS







favColor = "Red"
luckyNumber = 55
myGpa = 3.0
myAge = 16
pineappleOnPizza = True

# if Statements - Check for a condition to be True/False, do something if true.
if favColor == "Green":
    print("I like turtles")

if myAge >= 16:
    print("Go get a job!")

# if-else Statement -- Check for a condition, do something for 
if myGpa >= 3.0 :
    print("Congrulations on making the honor roll!")
else:
    print('Better luck next year. Try to study more!')

if luckyNumber >= 55 :
    print("Based Number Choice")
else:
    print("Bruh just get a better lucky number")

# if - else statements -- Checks for multiple conditions
if myAge > 64:
    print("Congratulations on retiring")
elif myAge > 50:
    print("Congratulations, you have earned a bonus of $1000!")
else:
    print("You are not old enough for a bonus")
# 1 if, 1 else, any number of elif allowed.

# Nested if - elif - else Statements
if myAge > 15:
    print("You are eligible for a license")
    if myGpa > 3.5:
        print("You qualify for a new car!")
    elif myGpa > 2.0:
        print("you qualify for $500 off a car!")
    else:
        print("You get nothing")
else:
    print("you are not old enough to drive")

# When doing if - elif - else statements, check for the highest values first!!!!
if myGpa >1.5:
    print("You are in danger of falling for they year")
elif myGpa > 2.0:
    print("You are on track to graduate")

# while Loop -- Think "MUSICAL CHAIRS" -- Used when you do NOT know how many iterations you need.
# iteration = one complete trip through a loop
x = 0
while x < 100:
    print(f"x is currently equal to {x}")
    x += 1

while x >= 0:
    print(f"x is currently equal to {x}")
    x -= 1

# for Loop -- Thnik 'Go Fish', used when you know number of iterations needed
print("FOR LOOP STARTS HERE")
for i in range(10): # 1 = iterable
    print(i)

print("EVEN OR ODD LOOP!")
for i in range(101):
    print(i)
    if i % 2 == 0:
        print("That number is even!")
    else:
        print("That number is odd!")

# () Parentheses
# [] Square Brackets
# <> Angle Brackets
# {} Braces