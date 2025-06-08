# sname = "Gouri Prasad Mahapatra"

# splitN = sname.split(" ")

# for nm in splitN:
#     print(nm)

# # for nm in sname:
# #     print(nm)

# text = "Gouri"
# num = [1,2,3,4,5]

# for st, number in zip(text, num):
#     print(st, number)

#Used to iterate over a sequence (like a list, tuple, dictionary, set, or string).

# for item in [1, 2, 3]:
#     print(item)

# lst = [3,4,5,6,7,8]
# for it in lst:
#     print(it)

# for i in range(9):
#     print(i)

#while condition satisfied

count = 11

# while count <= 9:
#     print(count)
#     count = count + 1

# while count > 10:
#     if count == 20:
#         break
#     else:
#         count = count + 1
#     print (count)

# def evenOdd(number):
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("odd") 

# evenOdd(1)

def table(n, counter):
    if counter == 12 :
        return []
    else:
        #print(f"{n}*{counter+1}={n * (counter+1)}")
        result = f"{n}*{counter+1}={n * (counter+1)}"
        return [result] + table(n, counter+1)
    
result = table(5,0)
print(result)
        