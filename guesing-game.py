"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
"""

import random

userInput = int(input("Enter a number between 1 and 9: "))

num = random.randint(1, 9)

if userInput < num:
    print("You guesed too low")
elif userInput > num:
    print("You guesed too high")
else:
    print("You guesed the exact number!!")

print(num)