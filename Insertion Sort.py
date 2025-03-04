#Insertion Sort..............
'''
Time Complexity = O(n**2)
Space Complexity = O(1)
'''
def insertionSort(lis):
    for i in range(1,len(lis)):
        temp = lis[i]
        swap = i-1
        while swap>=0 and temp<lis[swap]:
            lis[swap+1] = lis[swap]
            swap-=1
        lis[swap+1] = temp
        print(*lis)
    return lis
print(*insertionSort(list(map(int,input().split()))))

'''
INPUT:
76 98 09 78 567 098 67 23
OUTPUT:
76 98 9 78 567 98 67 23
9 76 98 78 567 98 67 23
9 76 78 98 567 98 67 23
9 76 78 98 567 98 67 23
9 76 78 98 98 567 67 23
9 67 76 78 98 98 567 23
9 23 67 76 78 98 98 567
9 23 67 76 78 98 98 567
'''
