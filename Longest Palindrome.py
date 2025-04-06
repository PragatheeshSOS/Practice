# Longest Palindrome.........
string = input()
counter,res = [],0
for i in set(string):
    counting = string.count(i)
    if counting%2:
        counter.append(counting)
    else:
        res+=counting
print(res+1) if counter else print(res)
'''
INPUT:
abab
OUTPUT:
4
INPUT:
abbccccxy
OUTPUT:
7
'''
