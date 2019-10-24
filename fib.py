# Author: Zihan Li
# Date: 22/10/2019
# Description: takes a positive integer parameter and returns the number at that position of the Fibonacci sequence.

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)


print("Enter n:")
n = int(input())
print(fib(n))
