"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
"""

num = int(input("Please choose a number to divide: "))

listRange = list(range(1, num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

if len(divisorList) > 2:
    print(str(num)+' is not a prime number')
else:
    print(str(num)+' is a prime number')

print(divisorList)
