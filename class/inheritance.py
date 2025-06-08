class Person:
    def __init__(self, Name,Age):
        self.name = Name
        self.age = Age
    def printName(self):
        print(f"Name :{self.name}:{self.age}")

p = Person("Name",45)
print(p.name)

class Student(Person):
    pass
    def Age(self):
        print("Age is : 7")

s = Student("Gouri", 55)

s.printName()
