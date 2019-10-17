# Author: Zihan Li
# Date: 16/10/2019
# Description: asks the user how many integers they would like to enter， then displays the largest and smallest of those numbers

number = 0
val = 0
min = 0
max = 0

print('How many integers would you like to enter?')
size = int(input())
print('Please enter ', size, ' integers.')
number = int(input())

min = number
max = number

while val < size - 1:
    number = int(input(''))
    if number < min:
        min = number

    if number > max:
        max = number

    val = val + 1

print('min:', min)
print('max:', max)
