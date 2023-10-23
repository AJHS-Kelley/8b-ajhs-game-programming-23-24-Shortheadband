#Collections GA v0.4

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

#weaponList = [
    
    #True, # Gun
    #True, # Knife
    #False, # Ultra Gun
    #False, # Mighty Knife
    #]
    
#weaponNum = 0
#while weaponNum < len(weaponList):
    #if weaponNum == 0 and weaponList[0] == True:
           #print("you are wielding a Gun.\n")
    #if weaponNum == 1 and weaponList[1] == True:
            #print("you are wielding a Knife.\n")
    #if weaponNum == 2 and weaponList[2] == True:
            #print("you are wielding a Ultra Gun.\n")
    #if weaponNum == 3 and weaponList[3] == True:
            #print("you are wielding a Mighty Knife.\n")
    #weaponNum += 1    

#Item Exists in Inventory

#doorkeys = [
   # "red",
   # "green",
   # "yellow",
   # "purple",
   # "brown",

#  ]

# key = input("which color key doy need to unlock the door?\n")

# if key in doorkeys:
 #   print("you have the correct key! The door unlocks.\n")
# else:
 #   print("you do not have that key. The door remains locked")

#Random Enemy Genrator

enemyBase = ["demon","slime","skeletion","goblin","Ork"]
enemyType = ["Necromancer","Mage","Scout","Archer","Crusader"]
enemyPrefix = ["Elite","Tainted","enlightened","Super Elite","Alpha","Rookie"]

import random 

reb = random.randint(0,len(enemyBase))
ret = random.randint(0,len(enemyType))
rep = random.randint(0,len(enemyPrefix))
enemy = (print(reb),print(ret),print(rep))
i = 0
while i <= 15:

    print(f"A {enemy} is approaching")
i + (i + 1)
