# Author: Zihan Li
# Date: 20/11/2019
# Description:  a function named count_letters that takes as a parameter a string and returns a dictionary
#               that tabulates how many of each letter is in that string


def count_letters(string):
    letters_dic = {}
    for l in string.upper():
        if l.isalpha():
            if l in letters_dic:
                letters_dic[l] += 1
            else:
                letters_dic[l] = 1
    return letters_dic
