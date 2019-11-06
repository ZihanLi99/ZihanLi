# Author: Zihan Li
# Date: 5/11/2019
# Description: a function should return the median of those numbers, which will require it to sort the list

def find_median(num_list):
    num_list.sort()
    if(len(num_list) % 2 == 1):
        return num_list[len(num_list) // 2]
    else:
        return (num_list[len(num_list) // 2 - 1] + num_list[len(num_list) // 2]) / 2
