# QUESTION............
# Given a string S, print the minimum number of characters you have to remove from the string S to make it a clean string. A clean string is a string in which all the characters are distinct.

string = input()
print(len(string)-len(set(string)))

'''
INPUT:
aabc
OUTPUT:
1

INPUT:
q1
OUTPUT:
0
'''
