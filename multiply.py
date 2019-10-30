# Author: Zihan Li
# Date: 29/10/2019
# Description: a recursive function named multiply that takes two positive integers as parameters and returns the product of those two numbers 

def multiply(a,b):

    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)
