# Author: Zihan Li
# Date: 2020/2/11
# Description: a recursive function named is_decreasing that takes as its parameter a list of numbers


def is_decreasing(num_list):
    return check_decreasing(num_list, 0, len(num_list) - 1)
    # return a new list that is the reverse of num_list

def check_decreasing(num_list, f_num, n_num):
    if f_num < n_num:
        if num_list[f_num] < num_list[f_num + 1]:
            # compare the first number with the next number
            return False
        else:
            return check_decreasing(num_list, f_num + 1, n_num)
            # if bigger, return the next set to compare
    else:
        return True
