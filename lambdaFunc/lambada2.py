
def increment():
    return lambda x: x+ 1

f = increment()

print(f(66))