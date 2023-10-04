# Adding items

playerInventory = []

i = 1
while i <= 10:
    item = input("Add item .\n")
    playerInventory.append(item)
    i += 1

playerInventory.sort()
print(f"The player's inventory is {playerInventory}.")

# Removing items

#i = 1
#while 1 >= 5:
 #   print(i)
  #  i -= 1

#playerInventory.sort()
#print(f"The player's inventory is {playerInventory}.")