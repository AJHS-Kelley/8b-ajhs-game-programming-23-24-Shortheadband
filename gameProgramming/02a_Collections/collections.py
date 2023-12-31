#Collections Examples, Ryan Kelley, v0.5a

# LIST -- ORDERED, CHANGEABLE, ALLOWS CUPLICATE VALUES
#breakfastfoods = ["Bacon","Waffles","Pancakes", "Cereal", "Milk"]
# Each item on the list known as an ELEMENT.
# The position in the list for each is the INDEX
# The element "BACON" is at index 0.
# Python Only: index -1 it is the last item on the list
#testScores = [95,100,25,15,27,35]
#classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25]

# Printing Contents of an Lists
#print(breakfastfoods)
#print(testScores)
#print(classGPA)

# Accessing Specfic List Elements -- REMEMBER FIRST ELEMENT IS INDEX 0
#print(breakfastfoods[0])
#print(testScores[0])
#print(classGPA[0])

# Accessing Last Element in Lists
#print(breakfastfoods[-1])
#print(testScores[-1])
#print(classGPA[-1])

#pause - WYOC -- Access the 3rd Element in Each List
#print(breakfastfoods[2])
#print(testScores[2])
#print(classGPA[2])

# Changing Items in a List
#breakfastfoods[0] = "Sausage"
#testScores[0] = 97
#classGPA[0] = 3.57
#print(breakfastfoods[0])
#print(testScores[0])
#print(classGPA[0])
#print(breakfastfoods)
#print(testScores)
#print(classGPA)

# Pause -- WYOC -- Change 5th Element
#breakfastfoods[4] = "Bagel"
#testScores[4] = 45
#classGPA[4] = 2.45
#print(breakfastfoods)
#print(testScores)
#print(classGPA)

# Adding and Inserting Items to a List
# .append() adds an item to the end
#breakfastfoods.append("hash browns")
#print(breakfastfoods)
#testScores.append(99)
#print(testScores)
#classGPA.append(1.99)
#print(classGPA)

# .insert() allows you to place an item at a specfic index in the list
#breakfastfoods.insert(3, "parfait")
#print(breakfastfoods)
#testScores.Insert(3, 55)
#print(testScores)
#classGPA.Insert(3, 0.0)
#print(classGPA)

# Pause -- WYOC -- .apprnd() another item to each list. .insert() an item at index 5 to each list.
#breakfastfoods.append("Honey Bun")
#print(breakfastfoods)
#testScores.append(100)
#print(testScores)
#classGPA.append(4.0)
#print(classGPA)

# Deleting Items from a List
# Use .romove() to remove a specfic item from the list.
#breakfastfoods.remove("Waffles")
#print(breakfastfoods)
#testScores.remove(100)
#print(testScores)
#classGPA.remove(2.25)
#print(classGPA)

# To delete using the index value we use .pop()
#breakfastfoods.pop(4)
#print(breakfastfoods)
#testScores.pop(4)
#print(testScores)
#classGPA.pop(4)
#print(classGPA)

# PAUSE - WYOC -- .pop() the 2nd element from each list.
#breakfastfoods.remove("Bacon")
#print(breakfastfoods)
#testScores.remove(100)
#print(testScores)
#classGPA.remove(2.25)
#print(classGPA)

# Determining List Length
#print(f"There are {len(breakfastfoods)} items in the breakfastfoods list.")
#print(f"There are {len(testScores)} items in the testScores list.")
#print(f"There are {len(classGPA)} items in the classGPA list.")

# List Methods -- Functions for working with lists.
# Sorting Lists -- Alphanumerical -- Ascending -- Capital Letters before Lower Case Letters
#print(f"The original breakfastFoods list is {breakfastfoods}")
#breakfastfoods.sort()
#print(f"The Sorted breakfastfoods list is {breakfastfoods}.")
#print(f"The original testScores list is {testScores}")
#testScores.sort()
#print(f"The Sorted testScores list is {testScores}.")
#print(f"The original classGPA list is {classGPA}")
#classGPA.sort()
#print(f"The Sorted testScores list is {classGPA}.")

breakfastfoods = ["Bacon","Waffles","Pancakes", "Cereal", "Milk", "Bacon"]
testScores = [95,100,25,15,27,35,100]
classGPA = [3.14, 2.25, 1.74, 1.99, 0.99, 4.25, 1.74]

# .count() will return the number of times a value appears in a list.
#numWaffles = breakfastfoods.count("Waffles")
#print(f"There are {numWaffles} waffles in the list.")
#numBacon = breakfastfoods.count("Bacon")
#print(f"There are {numBacon} Bacon in the list.")
# Pause -- WYOC -- use .count() to count for a single item in the list and any multiple items. Use testScores and classGPA

#numScores = testScores.count(100)
#print(f"There are {numScores} students with a score of 100 in the list.")
#numGPA = classGPA.count(1.74)
#print(f"There are {numGPA} students with a GPA of 1.74 in the list.")

# Deleting All Contents of a list -- .clear()
#breakfastfoods.clear
#print(f" The breakfastfoods list is {breakfastfoods}.")
#testScores.clear
#print(f"The testScores list is {testScores}.")
#classGPA.clear()
#print(f" The classGPA list is {classGPA}.")

# Common Nugs -- Index out of range
print(f"The last item in the list is {breakfastfoods[0]}.")

print(f"The last item in the testScores list is {testScores[len(testScores)- 1]}")

