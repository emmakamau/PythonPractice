"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

def fibonacci():
    sequence = []
    max = int(input("How many Fibonnacci numbers do you need? "))
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    sum = a+b

    sequence.append(a)
    sequence.append(b)
    sequence.append(sum)

    for i in sequence:
        if len(sequence) < max:
            sum = sequence[len(sequence)-2] +sequence[len(sequence)-1]
            sequence.append(sum)
    print(sequence)

fibonacci()
