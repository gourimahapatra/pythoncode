

def binarySearch(arr, targetVal):
    left = 0
    right = len(slist)-1

    while (left <= right ):
        mid = (left + right)/2
        if(arr[mid] == targetVal):
            return mid
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid-1
    return -1

slist = [3,4,5,6,7,8,9,10]

x = 9

result = binarySearch(slist,x)

print(result)