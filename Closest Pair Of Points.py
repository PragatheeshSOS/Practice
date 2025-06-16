# Closest Pair Of Points.....................................................
size = int(input())
lis = sorted(list(map(int,input().split())))
res = float('inf')
for i in range(size-1):
    diff = abs(lis[i]-lis[i+1])
    if diff<res:
        res = diff
print(res)
'''
INPUT:
3
-10 0 11
OUTPUT:
10

INPUT:
5
10 2 -4 5 29
OUTPUT:
3
'''
