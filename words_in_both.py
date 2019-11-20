# Author: Zihan Li
# Date: 20/11/2019
# Description:  a function named words_in_both that takes two strings as parameters and returns a
#               set of the words contained in both strings


def words_in_both(wib1, wib2):
    word1 = wib1.lower().split(" ")
    word2 = wib2.lower().split(" ")
    same_w = []
    for w in word1:
        if (w in word2) and (w not in same_w):
            same_w.append(w)
    return same_w
