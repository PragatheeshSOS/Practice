#Smallest Pair Factors........................
# QUESTION.............
# You are given an integer N denoting whose pair factors are A and B. You have to find the minimum value of A+B for any integer A and B.
# Example:
# N=96
# The pair factors of 96 are (1, 96), (2, 48), (3, 32), (4, 24), (6, 16), (8, 12).
# Min(A+B) = 8+12 = 20
# Note: Value of N is  1<=N<=10^13 (long long int)
number = int(input())
res = float('inf')
for i in range(1,int(number**0.5)+1):
    if number%i == 0:
        remain = number//i
        res = min(res,remain+i)
print(res)
'''
Sample Input
96
Sample Output
20
'''
