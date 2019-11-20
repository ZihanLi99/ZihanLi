# Author: Zihan Li
# Date: 20/11/2019
# Description:  a function named count_letters that takes as a parameter a string and returns a dictionary
#               that tabulates how many of each letter is in that string


def count_letters(string):
    cl = {}
    for le in string.upper():
        if le in cl:
            cl[le] += 1
        else:
            cl[le] = 1
    return cl
