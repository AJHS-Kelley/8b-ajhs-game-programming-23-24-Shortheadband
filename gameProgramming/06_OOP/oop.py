# object - oritented Programming, Gabriel Coffey, v0.0

class Person: # Yse PascalCalse for ClassNames 
    def   __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    #
    def __str__(self):
        return f"Name: {self.name}\nThis persson is {self.age} years old\nThey weigh {self.weight} pounds.\n"



person1 = Person("Nash", 25, 160.1)
person2 = Person("Eli", 27, 154.8)
print(person1)
print(person2)

if person1.weight > person2.weight:
    print(f"{person1.name} weighs more than {person2.name}.")
elif person1.weight == person2.weight:
    print("Each person weighs the same.\n")
else:
    print(f"{person2.name} weighs more than {person1.name}.")

if person1.age > person2.age:
    print(f"{person1.name} is older than {person2.name}.")
elif person1.age == person2.age:
    print("Each person are the same age.\n")
else:
    print(f"{person2.name} is older than {person1.name}.")
