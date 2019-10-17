# Author: Zihan Li
# Date: 14/10/2019
# Description: asks the user to enter a positive integer, then prints a list of all positive integers that divide that number evenly

print("Please enter a positive integer: ")
num = int(input())
print("The factors of", num, "are:")

for i in range(2, num):
    if num % i == 0:
        print(i)
