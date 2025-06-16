# Palindrome Or Not After Expanding....................................................
string = input()
res = ""
for i in range(len(string)):
    if string[i].isalpha():
        alpha = string[i]
        count,index = "",i+1
        while index<len(string) and string[index].isnumeric():
            count+=string[index]
            index+=1
        res+=(alpha*int(count))
print("PALINDROME" if res == res[::-1] else "NOT A PALINDROME")
'''
INPUT:
A10B1A10
OUTPUT:
PALINDROME
INPUT:
A9A1B1A10
OUTPUT:
PALINDROME
INPUT:
A9A1B1A9
OUTPUT:
NOT A PALINDROME
'''
