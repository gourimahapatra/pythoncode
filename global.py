#global variable
c = 1

def add(x):
    global c
    c = 90
    
    a = c+ x
    return a

print(add(6))
print(c)