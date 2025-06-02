def rotate_right(arr, k):
    return arr[-k:] + arr[:-k]
arr = [1, 2, 3, 4, 5,6]
rotated = rotate_right(arr, 5)
print(rotated)

