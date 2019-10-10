# Author: Zihan Li
# Date: 9/10/2019
# Description: asks the user for a (integer) number of cents,
#              from 0 to 99, and outputs how many of each type of coin
#              would represent that amount with the fewest total number of coins.

print("Please enter an amount in cents less than a doller.")
cent = eval(input())
print("Your change will be:")
print("Q:", cent // 25)
cent = cent % 25
print("D:", cent // 10)
cent = cent % 10
print("N:", cent // 5)
cent = cent % 5
print("P:", cent)
