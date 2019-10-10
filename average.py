# Author: Zihan Li
# Date: 8/10/2019
# Description: asks the user for five numbers and then prints out the average of those numbers. 

print("Please enter five numbers.")
total = 0
for x in range(5):
    total += eval(input())
    
print("The average of those nunmbers is:")
print(total/5)
