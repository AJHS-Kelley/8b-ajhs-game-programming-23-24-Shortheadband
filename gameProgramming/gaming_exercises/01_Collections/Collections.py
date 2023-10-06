#Collections GA v0.1

# Adding items

playerInventory = []

i = 1
while i <= 10:
    item = input(f"Add item {i} .\n")
    playerInventory.insert(i,item)
    i += 1
    
playerInventory.sort()
print(f"The player's inventory is {playerInventory}.")

# Removing items

i = 2
while 2 >= -3:
   itemRemove = int(input(f"To remove an item input the NUMBER tied to it.\n"))
   isCorrect = input("Please type yes if correct, no if not correct.\n")
   if isCorrect == "yes":
    print(f"Ok, {playerInventory[itemRemove]} has been removed")
   playerInventory.pop(itemRemove)
   i -= 1

playerInventory.sort()
print(f"The player's inventory is {playerInventory}.")