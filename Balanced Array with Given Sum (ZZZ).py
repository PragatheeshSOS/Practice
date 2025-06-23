# Balanced Array with Given Sum (ZZZ).......................................................................................................................
'''
You are given an even integer N and an integer K.
Your task is to generate an array A of size N such that:
Each element Ai satisfies: 1 ≤ Ai ≤ 10⁵
The number of odd elements in the array is equal to the number of even elements
The sum of all elements in the array is exactly K
If multiple such arrays exist, print any.
If no such array exists, print -1.
🔸 Input Format:
The first line contains a single integer T — the number of test cases.
Each of the next T lines contains two space-separated integers N and K.
🔸 Output Format:
For each test case, output a line:
Either N space-separated integers (the array A)
Or -1 if it's not possible
🔸 Constraints:
1 ≤ T ≤ 1000
2 ≤ N ≤ 10⁵ and N is even
1 ≤ K ≤ 10⁹
The sum of all N over all test cases does not exceed 10⁶
🔸 Sample Input:
3
2 5
4 1
4 20
🔸 Sample Output:
3 2
-1
15 2 1 2
🔸 Explanation:
Test 1: Array [3,2] has 1 odd, 1 even; sum = 5 ✅
Test 2: No such array possible with 4 elements and total sum 1 ❌
Test 3: [15, 2, 1, 2] has 2 odds (15,1) and 2 evens (2,2); sum = 20 ✅
'''
import sys
data = sys.stdin.read().split()
t = int(data[0])
index = 1
results = []
for _ in range(t):
    N = int(data[index])
    K = int(data[index + 1])
    index += 2
    min_sum = 3 * N // 2
    max_sum = (N // 2) * 199999
    if K < min_sum or K > max_sum:
        results.append("-1")
        continue
    D = K - min_sum
    if D % 2 != 0:
        results.append("-1")
        continue
    n_half = N // 2
    odd_list = [1] * n_half
    even_list = [2] * n_half
    rem = D
    for i in range(n_half):
        if rem <= 0:
            break
        add = min(rem, 99998)
        odd_list[i] += add
        rem -= add
    for i in range(n_half):
        if rem <= 0:
            break
        add = min(rem, 99998)
        even_list[i] += add
        rem -= add
    res_list = []
    for i in range(n_half):
        res_list.append(str(odd_list[i]))
        res_list.append(str(even_list[i]))
    results.append(" ".join(res_list))
print("\n".join(results))
'''
INPUT:	
3
2 5
4 1
4 20
OUTPUT:
3 2
-1
15 2 1 2

INPUT:
2
3 2
4 1
OUTPUT:
-1
-1

INPUT:
1
100 150
OUTPUT:
1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2
'''
