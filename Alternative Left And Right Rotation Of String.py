# Alternative Left And Right Rotation Of String..........................................................................................
for i in range(int(input())):
    string,pos = input(),int(input())
    print(string[len(string)-pos:]+string[:len(string)-pos]) if i%2 else print(string[pos:]+string[:pos])
'''
INPUT:
5
Hello
1
Hello
1
ITVAC
2
ITVAC
2
Mercel
0
OUTPUT:
elloH
oHell
VACIT
ACITV
Mercel
'''
