# Methods are functions that belong to objects.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.say_hello()

print()

# Object properties can be changed after creation.
p1.age = 4
print(p1.age)
