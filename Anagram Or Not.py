# Anagram Or Not................................................................................
for _ in range(int(input())):
    string1,string2 = map(str,input().split())
    print(sorted(list(string1)) == sorted(list(string2)))
'''
INPUT:
Hello hello
hello hello
HELLO hello
OUTPUT:
False
True
False
'''
