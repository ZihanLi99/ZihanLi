# Author: Zihan Li
# Date: 20/11/2019
# Description:  a function named count_letters that takes as a parameter a string and returns a dictionary
#               that tabulates how many of each letter is in that string


def count_letters(string):
    cletter_dic = {}
    for l in string.upper():
        if l in cletter_dic:
            cletter_dic[l] += 1
        else:
            cletter_dic[l] = 1
    return cletter_dic
