def nthLarget(lst,n):
    uniqueList = list(set(lst))
    if n > len(uniqueList):
        return None
    sortedList = sorted(uniqueList, reverse=True)
    print(sortedList)
    return sortedList[n-1]

lst = [4,5,6,7,2,1,3,9,8,7]

print(nthLarget(lst,1))
