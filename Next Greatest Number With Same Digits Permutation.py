# Next Greatest Number With Same Digits Permutation...................................................................................................................
'''Given a number 'N' (containing at most 10,000 digits), find the next greater number having the same digits. It is guaranteed that there exists a next greater number having the same digits as N.
Input specification:
Input: the number 'N' in the form of a string.
Output specification:
Return the next greater number having the same digits as 'N' in the form of a string
Example:
Input:
182
Output:
218
Explanation:
Using the same digit the number of permutation are:
128
182
218
281
Example 2:
Input:
1234567849876554321
Output:
1234567851234456789
Input Format
Input: the number 'N' in the form of a string.
Output Format
Return the next greater number having the same digits as 'N' in the form of a string
Sample Input 1
5
23456
Sample Output 1
Next number with same set of digits is 23465
Sample Input 2
3
000
Sample Output 2
Not possible
'''
from itertools import permutations
number = input().strip()
num = int(number)
perms = set(int(''.join(p)) for p in permutations(number))
res = sorted([p for p in perms if p>num])
print("Next number with same set of digits is", res[0]) if res else print("Not possible")
'''
INPUT:
23456
OUTPUT:
Next number with same set of digits is 23465

INPUT:
182
OUTPUT:
Next number with same set of digits is 218

INPUT:
0
OUTPUT:
Not possible

INPUT:
4432
OUTPUT:
Not possible
'''
