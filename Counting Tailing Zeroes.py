# Counting Tailing Zeroes...............
# QUESTION................
# For each integer m find number of n such that the factorial of n ends with exactly m zeroes.
# Input First line of input contains an integer T number of test cases. Each test case contains an integer M (1 ≤ M ≤ 100,000) — the required number of trailing zeroes in factorial.
# Output First print k — the number of values of n such that the factorial of n ends with m zeroes. Then print these k integers in increasing order.
# *** It is a time complexity question, so the output should be efficient and should be within 1 ms ***

def zeros(fact):   # This Function Helps The Factorial (Avoid Direct Factorial Function Used). Efficient.!!
    zero = 0              # fact = 25 zero= 0
    while fact>0:         # zero+=25//5 => 5 (From Numbers Like 5,10,15,20,25)
        fact//=5          # zero+=25//25 => 1 (25 Adds One Extra 5)
        zero+=fact        # zero+=25//125 => 0 (We Stop Here)
    return zero           # zero = 6 (Total Tailing Zeroes Is 6)

for _ in range(int(input())): # Testcases
    target = int(input())   # Target Tailing Zeroes
    left,right,res = 0,(target*5)+5,0
    while left<=right:
        mid = (left+right)//2
        zero = zeros(mid)
        if zero == target:    # Confirming Target Tailing Are Gotten.
            res = mid
            right = mid-1     # Resetting To Find Smallest Value.
        elif zero>target:
            right = mid-1
        else:
            left = mid+1
    if res:
        print(5)
        print(*[i for i in range(res,res+5)])
    else:
        print(0)

'''
INPUT:
1
1
OUTPUT:
5
5 6 7 8 9

INPUT:
10
235
679
729
738
738
661
506
802
210
642

OUTPUT:
0
5
2725 2726 2727 2728 2729
5
2925 2926 2927 2928 2929
5
2965 2966 2967 2968 2969
5
2965 2966 2967 2968 2969
5
2650 2651 2652 2653 2654
5
2030 2031 2032 2033 2034
5
3215 3216 3217 3218 3219
0
5
2575 2576 2577 2578 2579
'''
