# object - oritented Programming, Gabriel Coffey, v0.0

class Person: # Yse PascalCalse for ClassNames 
    def   __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    #
    def __str__(self):
        return f"Name: {self.name}\nThis persson is {self.age} years olf\nThey weigh {self.weight} pounds.\n"



person1 = Person("Nash", 25, 160.1)
print(person1)        