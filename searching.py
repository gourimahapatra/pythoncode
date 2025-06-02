# sName = "Gouri Prasad Mahapatra"
# #return True/False
# print("Gofuri" in sName)
# #Return Index or 
# index = sName.find("Prasad")
# print(index)

# indx = sName.index("Prasad")
# print(indx)

#Difference between index and Find
# Feature	.find()	.index()
# Found	Returns index	Returns index
# Not Found	Returns -1	Raises ValueError
# Use Case	Safer, no error	Stricter, raises error

# text = "data.csv"
# print(text.startswith("data"))# True
# print(text.endswith(".csv"))# True

str1 = "Gouri Prasad Prasadclear"
str2 = "Prasad"

index = str1.find(str2)
print(index)

