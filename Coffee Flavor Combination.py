#Coffee Flavor Combination.........
import math
flav,comb,res = int(input()),int(input()),0
for i in range(1,comb+1):
    res+= (math.factorial(flav)//(math.factorial(i)*math.factorial(flav-i)))
print(res)
'''
INPUT:
5
2
OUTPUT:
15
INPUT:
10
1
OUTPUT:
10
'''
