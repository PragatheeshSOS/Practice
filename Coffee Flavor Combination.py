#Coffee Flavor Combination.........
import math
flav,comb,res = int(input()),int(input()),0
for i in range(1,comb+1):
    res+= (math.factorial(flav)//(math.factorial(i)*math.factorial(flav-i)))
print(res)

#If Combination Library Works.....
import math
n = int(input())
print(math.comb(n,int(input())) + n)
# If Above One Fails Testcases.
import math
n,k,res = int(input()),int(input()),0
for i in range(1,k+1):
    res+=math.comb(n,i)
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
'''
Combination Mathematical Formula:
comb(n,k) = n! // k!(n-k)!
For Program, We Replace k with iterative i (From 1 to k+1) (i.e).
comb(n,k) = n! // i!(n-i)! Where i iterative loop from 1 to k+1
'''
