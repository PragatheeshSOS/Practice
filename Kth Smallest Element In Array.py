#Kth Smallest Element In Array............
#Approach 1............... (Array Shoud Contain Unqiue Elements)
lis = list(map(int,input().split()))
lis.sort()
print(lis[int(input())-1])
'''
Time Complexity = O(n log(n))
Space Complexity = O(n)
'''

#Approach 2.............. (Works For Duplicate Elements Too)
def KthSmallestElement(lis,count):
    lis.sort()
    i = 0
    while i<len(lis):
        while i<len(lis)-1 and lis[i] == lis[i+1]:
            i+=1
        count-=1
        if count == 0:
            return lis[i]
        i+=1
        
print(KthSmallestElement(list(map(int,input().split())),int(input())))
'''
Time Complexity = O(n log(n))
Space Complexity = O(n)
'''
'''
INPUT:
1 2 3 4 5 6
4
OUTPUT:
4

INPUT:
1 8 9 3 0
3
OUTPUT:
3

INPUT:
9 0 8 19
3
OUTPUT:
9
'''
