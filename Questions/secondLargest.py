def secondLargest(lst):
    if len(lst) < 2:
        print("not suffcient otems")
    else:
        tLst = sorted(lst)
        return tLst[1]
    
print(secondLargest([23,34,667,]))

#Optimize
def secondLargest(lst):
    if len(lst) < 2:
        print("not sufficient items")
        return None
    tLst = list(set(lst))  # Remove duplicates
    if len(tLst) < 2:
        print("not enough unique items")
        return None
    tLst.sort()
    return tLst[-2]

print(secondLargest([23,34,667]))