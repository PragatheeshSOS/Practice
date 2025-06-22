# Smallest Number In Number String By Removing K Times...............................................................................
'''
Given a non-negative integer num represented as a string, remove any k (need not be consecutive numbers) digits from the number so that the new number is the smallest possible.
Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left
For example:
Input	Result
10200
1
200
8577
2
57
'''
stack = []
number = input()
size = int(input())
for i in number:
    while stack and size>0 and stack[-1]>i:
        stack.pop()
        size-=1
    stack.append(i)
while size>0:
    stack.pop()
    size-=1
res = "".join(stack).lstrip('0')
print(res)
'''
INPUT:
10200
1
OUTPUT:
200

INPUT:
8577
2
OUTPUT:
57
'''
