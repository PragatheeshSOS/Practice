#Reverse Alphabets In A String Without Reversing Special Character, Comma And Space.
given = list(input("Enter String: "))
lis = [i for i in given if i.isalpha()]
for i in range(len(given)):
    if given[i].isalpha():
        given[i] = lis.pop()
print("".join([i for i in given]))
'''
INPUT:
Enter String: *I'll given a string
OUTPUT:
*g'ni rtsan e vigllI

INPUT:
Enter String: I'll Be Back
OUTPUT:
k'ca Be BllI
'''
