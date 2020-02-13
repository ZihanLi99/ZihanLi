# Author: Zihan Li
# Date: 2020/2/11
# Description: a recursive function named array_max that takes as its parameter a list of
#              numbers and returns the maximum value in the list


def array_max(num_list):
    if len(num_list) == 1:
        return num_list[0]
        # if there is only one number
    else:
        if num_list[0] > array_max(num_list[1:]):
            return num_list[0]
        else:
            return array_max(num_list[1:])
    # use recursion to compare
