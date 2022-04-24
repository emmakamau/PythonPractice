"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
"""

sentence = input("Type a sentence")

def fun():
    split_sentence= sentence.split(" ")
    new_sentence= split_sentence[-1::-1]
    final_sentence = " ".join(new_sentence)
    print (final_sentence)

fun()