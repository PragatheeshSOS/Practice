# Quick Sort....................................................................
# Partition...............................
def partition(lis, low, high):
    swapIndex = low
    pivot = lis[high]
    for i in range(low,high):
        if lis[i]<pivot:
            lis[i],lis[swapIndex] = lis[swapIndex],lis[i]
            swapIndex+=1
    lis[swapIndex],lis[high] = lis[high],lis[swapIndex]
    return swapIndex

# Quicksort.....................
def quicksort(lis,low,high):
    if low<high:
        part = partition(lis,low,high)
        quicksort(lis,low,part-1)
        quicksort(lis,part+1,high)

# Main.................
lis = list(input().split())
quicksort(lis,0,len(lis)-1)
print(*lis)
'''
INPUT:
0 2 1 3 5
OUTPUT:
0 1 2 3 5

INPUT:
apple banana grape cherry
OUTPUT:             
apple banana cherry grape

INPUT:
[]
OUTPUT:
[]

INPUT:
43
OUTPUT:
43

INPUT:
4 5 4 3 2 5 1
OUTPUT:
1 2 3 4 4 5 5

INPUT:
10 3 76 34 23 32 100 1
OUTPUT:
1 3 10 23 32 34 76 100

INPUT:
3 -1 0 -5 8
OUTPUT:
-5 -1 0 3 8

INPUT:
9 8 7 6 5
OUTPUT:
5 6 7 8 9

INPUT:
1 2 3 4 5
OUTPUT:
1 2 3 4 5

INPUT:
7 7 7 7 7 7 7
OUTPUT:
7 7 7 7 7 7 7
'''
