# Replacing ? To Alphabet.................
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
string = list(input())
if len(string)<26:
    print(-1)
else:
    for i in string:
        if i not in ['?'] and alpha!=[]:
            print(i,end="")
            alpha.pop(0)
        elif i in ['?'] and alpha!=[]:
            print(alpha.pop(0),end="")
        else:
            print(i,end="")
'''
INPUT:
abcdefghijklmnopqrst??yz
OUTPUT:
-1

INPUT:
abcd??ghijklmnop??????wx?yz
OUTPUT:
abcdefghijklmnopqrstuvwxyyz
'''
