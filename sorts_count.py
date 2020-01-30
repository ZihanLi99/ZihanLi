  
# Author: Zihan Li
# Date: 2020/1/29
# Description: a bubble sort that counts the number of comparisons and the number of exchanges made
#              while sorting a list and returns a tuple of the two values

def bubble_count(arr):
    # total count of comparision
    count = 0
    ex = 0
    # array length
    n = len(arr)
    # sort algorithm
    for i in range(n):
        for j in range(0, n - i - 1):
            # counting for comparision
            count += 1
            if arr[j] > arr[j + 1]:
                ex += 1
                t = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = t
    return count, ex


def insertion_count(arr):
    n = len(arr)
    # total count of comparision
    count = 0
    ex = 0
    # sort algorithm
    for i in range(1, n):
        key = arr[i]
        # start from i-1
        j = i - 1
        while j >= 0:
            # counting for comparision
            count += 1
            if key < arr[j]:
                ex += 1
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return count, ex
