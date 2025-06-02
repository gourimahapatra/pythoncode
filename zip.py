
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(name, score)

zipped = list(zip(names, scores))
print(zipped)



names = ['Alice', 'Bob', 'Charlie']# List of strings
ages = [25, 30, 22]# List of integers
is_active = [True, False, True] # List of booleans

# Zipping them together
for name, age, active in zip(names, ages, is_active):
    print(f"Name: {name}, Age: {age}, Active: {active}")

