# Author: Zihan Li
# Date: 16/10/2019
# Description: prompts the user for an integer that the player will try to guess.

print("Enter the number for the player to guess.")
num = int(input())
print("Enter your guess.")

guess_try = 1
guess = False

while (guess == False):
    guess_num = int(input())

    if (guess_num ==num):
        guess = True
        print("You guessed it in", guess_try, "tries")

    elif guess_num > num:
        print("Too high - try again:")

    else:
        print("Too low - try again:")

    guess_try = guess_try + 1
