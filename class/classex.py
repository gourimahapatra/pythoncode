# class emp:
#     x = 5

# e = emp()
# print(e.x)


class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    
    def myFunc(sdsd):
        print("My Function name is " + sdsd.name)

e = employee("unknown", 50)

print(e.age)
print(e.name)
e.age = 89
print(e.age)
print(e)
e.myFunc()
del e


