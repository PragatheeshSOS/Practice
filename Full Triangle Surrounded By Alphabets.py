#Full Triangle Surrounded By Alphabets.....
size = int(input())
for i in range(size):
    lis = []
    for j in range(size-i):
        print(chr(65+j),end="")
        lis.append(chr(65+j))
    print(str(" ")*(i*2),end="")
    print(*lis[::-1],sep="")
'''
INPUT - 7
OUTPUT
ABCDEFGGFEDCBA
ABCDEF  FEDCBA
ABCDE    EDCBA
ABCD      DCBA
ABC        CBA
AB          BA
A            A
'''
