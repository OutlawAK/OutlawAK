import math
arr = [1, 2, 3, 4, 5, 6]


def arr_rev():

    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-i-1]
        arr[len(arr)-i-1] = temp
    print(arr)


def min_max(arr):
    count = 0
    max = 1
    min = 1
    for i in range(len(arr)):

        count += 1
    return min, max, count


minimum, maximum, count = min_max(arr)
print(minimum, maximum, count)
