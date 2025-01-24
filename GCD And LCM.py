#GCD And LCM......
import math
for _ in range(int(input())):
    num1,num2 = map(int,input().split())
    print(abs(num1*num2)//math.gcd(num1,num2),math.gcd(num1,num2),sep="\n")
'''
INPUT:
3
12 24
35 50
10 15
OUTPUT:
24
12
350
5
30
5

INPUT:
1
24 18
OUTPUT:
72
6

INPUT:
4
10 35
44 79
7 14
3 19
OUTPUT:
70
5
3476
1
14
7
57
1
'''
