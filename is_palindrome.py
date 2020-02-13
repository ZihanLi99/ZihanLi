# Author: Zihan Li
# Date: 2020/2/12
# Description: Write a recursive function named is_palindrome that takes as its parameter a string.
#              It should return True if that string is a palindrome, but return False otherwise.

def is_palindrome(word_str):
    if len(word_str) == 1:
        # if there is only one letter, return True
        return True
    if word_str[0] != word_str[-1]:
        # compare the first and last letter
        return False
    return is_palindrome(word_str[1:-1])
