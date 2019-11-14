# Author: Zihan Li
# Date: 13/11/2019
# Description: a function named square_list that takes as a parameter a list and replaces
#               each value with the square of that value

def square_list(lst):
    for el in range(len(lst)):
        lst[el] = lst[el] * lst[el]
