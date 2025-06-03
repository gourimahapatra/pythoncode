def fact(x):
    if x == 1:
        return 1
    else:
        return (x * fact(x-1))
    

print(fact(4))

def addNumber(x):
    if x == 1:
        return 1;
    else:
        return x + addNumber(x-1)

print(addNumber(10))