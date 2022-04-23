"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
"""

#Soln1
a = [1,1,1,4,4,4,5,6,3,3,8,8,9,6,5,5]
b = list(dict.fromkeys(a))
c=[]
print(b)

#Soln2
for i in a:
    if i not in c:
        c.append(i)
print(c)

#Soln3
list=[]
[list.append(i) for i in a if i not in list]
print(list)

