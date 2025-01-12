# Binary Pattern...........
size = int(input())
for i in range(size):
    [print((i+j+1)%2,end="") for j in range(size)]
    print()
'''
INPUT:
4
OUTPUT:
1010
0101
1010
0101

INPUT:
2
OUTPUT:
10
01
'''
