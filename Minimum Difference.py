# Minimum Difference.....................................................
for _ in range(int(input())):
    size = int(input())
    lis = sorted(list(map(int,input().split())))
    res = float('inf')
    for i in range(1,len(lis)):
        res = min(res,abs(lis[i-1]-lis[i]))
    print(res)
'''
INPUT:
1
5
2 4 5 7 9
OUTPUT:
1

INPUT:
1
5
4 6 9 11 13
OUTPUT:
2

INPUT:
1
6
100 301 501 709 7878 2343
OUTPUT:
200
'''
