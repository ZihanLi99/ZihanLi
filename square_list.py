# Author: Zihan Li
# Date: 13/11/2019
# Description:  a function named reverse_list that takes as a parameter a
#               list and and reverses the order of the elements in that list.


def reverse_list(lst):
    m = 0
    n = len(lst) - 1
    while(m < n):
        t_lst = lst[m]
        lst[m] = lst[n]
        lst[n] = t_lst
        m += 1
        n -= 1
