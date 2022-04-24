"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password.
"""

import random
import array

def pass_gen():
    max_len = 10
    digits = ['0','1','2','3','4','5','6','7','8','9']
    lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    symbols = ['!','@','#','$','%','^','&','*','(','|','+','=']

    combine_list = digits+lower_case+upper_case+symbols

    random_digit = random.choice(digits)
    random_lowercase = random.choice(lower_case)
    random_uppercase = random.choice(upper_case)
    random_symbol = random.choice(symbols)

    temp_pass=random_digit+random_lowercase+random_uppercase+random_symbol

    for x in range(max_len - 4):
        temp_pass = temp_pass + random.choice(combine_list)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x  
    return password


def main():
    while True:
        print("Would you like a system generated password? Yes or No")
        query_ans = input().lower()
        if query_ans == "no":
            print("Bye bye... thank you for coming")
            print("-"*40)
        elif query_ans == "yes":
            print("In a moment")
            print("-"*40)
            password = pass_gen()
            print(f"Your password is {password}")
            print("-"*40)
        else:
            print("Din't quite get you, please enter yes or no")
            print("-"*40)

main()