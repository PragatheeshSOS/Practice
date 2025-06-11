# Longest Increasing Sequence.....................
arr = [int(input()) for _ in range(int(input()))]
dp = [1] * len(arr)
for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
'''
| Input | Result |
| ----- | ------ |
| 6     | 4      |
| 12    |        |
| 34    |        |
| 1     |        |
| 5     |        |
| 40    |        |
| 80    |        |
'''
