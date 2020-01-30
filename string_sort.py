# Author: Zihan Li
# Date: 2020/1/29
# Description: an insertion sort that sorts a list of strings instead of numbers

def string_sort(name_arr):
    name_list = []
    for l in range(len(name_arr)):
        name_list.append(name_arr[l].lower())
    name_arr = name_list
    # make all letters lowercase

    for l in range(1,len(name_arr)):
        # insertion sort
        temp = name_arr[l]
        L = l - 1
        while (L >= 0 and temp < name_arr[L]):
            name_arr[L + 1] = name_arr[L]
            L -= 1
        # sort them alphabetically
        name_arr[L + 1] = temp
    return name_arr
