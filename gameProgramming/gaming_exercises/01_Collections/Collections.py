#Collections GA v0.3

# Adding items

#playerInventory = []

#i = 0
#while i <= 9:
    #item = input(f"Add item {i} to your inventory .\n")
    #playerInventory.insert(i,item)
    #print(f"{item} has been added to your inventory.\n")
    #i = (i + 1)
    
#playerInventory.sort()
#print(f"The player's inventory is {playerInventory}.")

# Removing items

#i = 2
#while 2 >= -3:
   #itemRemove = int(input(f"To remove an item input the NUMBER tied to it.\n"))
   #isCorrect = input("Please type yes if correct, no if not correct.\n")
   #if isCorrect == "yes":
    #print(f"Ok, {playerInventory[itemRemove]} has been removed")
    #playerInventory.pop(itemRemove)
    #i -= 1
   #else:
        #print("Ok let's try that again.\n")
        #i = i

#layerInventory.sort()
#print(f"The player's inventory is {playerInventory}.")

# Fixed Inventory #
#print("Allow me to inspect your weapons.\n")

#weaponlist = ["sword", "daggers", "bow", "crossbow", "guantlets"]
#Weapons = len(weaponlist)

#for i in range(Weapons):
    #print(weaponlist[i])

#print(f"\nThis is but a shame,\n the level of your weapons still has more growing to do before I can add anything of value.")

#Item Exists in Inventory

doorKeys = ["violet"," red", "yellow","brown","blue"]
doors = ["red door", "blue door", "brown door", "yellow door", "violet door"]

#Key distrubution
doorNumber = 0
if doorNumber <= 1:
    doorKeys.insert(doorNumber,doorKeys[0])
    doors.insert(doorNumber,doors[0])
    doorNumber = doorNumber + 1
elif doorNumber <= 2:
    doorKeys.insert(doorNumber,doorKeys[1])
    doors.insert(doorNumber,doors[1])
    doorNumber = doorNumber + 1
elif doorNumber <= 3:
    doorKeys.insert(doorNumber,doorKeys[2])
    doors.insert(doorNumber,doors[2])
    doorNumber = doorNumber + 1
elif doorNumber <= 4:
    doorKeys.insert(doorNumber,doorKeys[3])
    doors.insert(doorNumber,doors[3])
    doorNumber = doorNumber + 1
elif doorNumber <= 5:
    doorKeys.insert(doorNumber,doorKeys[4])
    doors.insert(doorNumber,doors[4])
    doorNumber = doorNumber + 1

# Door Selector
import random
Door = random.randint(doors[0],doors[4])

print(f"so you've trapped yourself in a dunegeon let's see how you can get out of here.\n The {Door} appears before you.")

