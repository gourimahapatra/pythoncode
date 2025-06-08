# no1 = int(input("Enter 1st Number"))
# no2 = int(input("Enter 2nd Number"))

iFirstNo = 3
iSecNo = 6
if iFirstNo > iSecNo:
    print("First Number is greater")
elif iFirstNo == iSecNo:
    print("both are equal")
else:
    print("Sec. No is Greater")

val = max(iFirstNo,iSecNo, 78,70) 
print(val)

no1,no2,no3 = 42,41,43

if (no1> no2 and no2>no3):
    print("no1 Greater")
elif(no2> no1 and no2>no3):
    print("No 2 greater")
elif(no3> no1 and no3>no2):
    print( "no3 Greater")
else:
    print("All are equal")


a = "A"
b = "a"
if a == b :
    print("Both ar equal")
elif a > b:
    print("A is greater")
elif b > a:
    print("B is greater")
else:
    print("Don't know")






