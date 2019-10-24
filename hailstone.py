# Author: Zihan Li
# Date: 23/10/2019
# Description:  takes a positive integer parameter as the initial number of
#               a hailstone sequence and returns how many steps it takes to reach 1


def hailstone(num):
    if num % 2 == 0:
        return num = num // 2
    elif num % 2 == 1:
        return num = 3 * num + 1
    
print("Enter a number:")
num = hauilstone(int(input())

step = 1

while (num != 1)
    num = hailtone(num)
    step = step + 1
print(step)
