# Author: Zihan Li
# Date: 20/11/2019
# Description:  a function named count_letters that takes as a parameter a string and returns a dictionary
#               that tabulates how many of each letter is in that string


def count_letters(string):
    letter_dic = {}

    for c in string.upper():
        if c.isalpha():
            if c in letter_dic:
                letter_dic[c] += 1

            else:
                letter_dic[c] = 1

    return letter_dic
