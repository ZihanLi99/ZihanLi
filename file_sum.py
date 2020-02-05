# Author: Zihan Li
# Date: 2020/2/4
# Description: a function named file_sum that takes as a parameter the name of a text
#              file that contains a list of numbers, one to a line

def file_sum(file_name):
    sum = 0
    # instalize the data
    with open(file_name,'r') as infile:
    # open a file you want
        for num in infile:
            sum = sum + num
    # use loop to calculate sum of these number
    with open('sum.txt', 'w') as outfile:
        outfile.write("Sum = " + str(sum))
    # create a new file to show the sum
