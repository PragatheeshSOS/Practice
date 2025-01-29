#Finding Median............
import statistics
res = []
for _ in range(int(input())):
    res.append(int(input()))
    print(int(statistics.median(res)))
'''
INPUT:
4
5
15
1
3
OUTPUT:
5
10
5
4
'''
