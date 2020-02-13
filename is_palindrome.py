# Author: Zihan Li
# Date: 2020/2/12
# Description: Write a recursive function named is_palindrome that takes as its parameter a string

def isPalindrome(word_str):
    if len(word_str) == 1:
        # if there is only one letter, return True
        return True
    if word_str[0] != word_str[-1]:
        # compare the first and last letter
        return False
    return isPalindrome(word_str[1:-1])
