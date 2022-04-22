"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

word = input("Enter a word: ")

wordTwo = ""

for i in word:
    wordTwo = i + wordTwo
 
if (word == wordTwo):
    print(wordTwo+" is a palindrome of "+ word)
else:
    print("Opps! not palindromes")