#string slicing rule
#string[start:stop:step]


fName = "Gouri Prasad Mahapatra"
print(fName.proper())
sName = "Gouri|Prasad|Mahapatra|Munu"

# print(sName[4])

# print(sName[::])
# print(sName[0::])
# print(sName[0::1])
# print(sName[6::])
# print(sName[6::1])
# print(sName[0:6:])
# print(sName[::-1])
# print(sName[-3::-1])

# print(sName[5:10:2])
#print(sName[::-1])
listName = sName.split()
#print(listName)
listName = sName.split("|")
print(listName)

# for char in sName:
#     print(char)

for names in listName:
    print(names)
