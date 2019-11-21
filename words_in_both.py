# Author: Zihan Li
# Date: 20/11/2019
# Description:  a function named words_in_both that takes two strings as parameters and returns a
#               set of the words contained in both strings


def words_in_both(str1, str2):
    parts1 = str1.split()
    parts2 = str2.split()
    words = set()
    for part in parts1:
        words.add(part.lower())

    result = set()
    for part in parts2:
        part = part.lower()
        if part in words:
            result.add(part)
    return result
