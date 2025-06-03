x = (lambda a: a+10)(10)
print(x)
# The map() function applies the lambda function to each element in nums, resulting in a new list with squared values
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, nums))
print(result)

nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

numList = [5,6,7,8,9,10]

result = list(map(lambda y:y * 10,numList))
print(result)
fil = 70
filter = list(filter(lambda b:b> fil, result))
print(filter)

f = lambda x, y: x + y
result = f(2, 3)
print(result)

f = lambda x,y,z: x + y + z
print(f(10,90,34))

fSq = lambda x : x ** 2
print(fSq(7))

frem = lambda x: x if x % 2 == 0 else None
result = frem(6)
print(result)

greet = lambda: "Hello, World!"
result = greet()
print(result)

names = ["Alice", "Bob", "Charlie", "David"]
sorted_names = sorted(names, key=lambda x: x[-1])
print(sorted_names)
#print(names[-1])

result = lambda x:x + 1
print(result(2)) 