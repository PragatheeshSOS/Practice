# Partition Of Array Based On Pivot...................................................
lis = [int(input()) for _ in range(int(input()))]
pivot = int(input())
less,equal,high = [],[],[]
for i in lis:
    if i == pivot:
        equal.append(i)
    elif i>pivot:
        high.append(i)
    else:
        less.append(i)
less.sort(reverse=True)
high.sort(reverse=True)
print(*less+equal+high)
'''
INPUT:	
7
9
12
3
5
14
10
10
10
OUTPUT:
9 5 3 10 10 14 12

INPUT:
6
7
3
8
4
7
1
5
OUTPUT:
4 3 1 8 7 7
'''
