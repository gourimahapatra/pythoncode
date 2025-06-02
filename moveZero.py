#Move Zeroes

def arrangeZero(nlist):
    l3=[]
    zero=[]
    for l in nlist:
        if l == 0:
            zero.append(l)
        else:
            l3.append(l)
    return l3+zero

lst2=[3,0,3,0,9,0]
l1=[1,2,3,0,0,9,0]


print(arrangeZero(l1))
