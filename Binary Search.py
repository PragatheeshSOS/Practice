#BINARY SEARCH...........
'''
Time Complexity = O(log n)
Space Complexity = O(1)
'''
#Recursive Approach.......
def binary_search(lis,left,right,target):
    if left<=right:
        mid = (left+right)//2
        if target == lis[mid]:
            return mid
        if target>lis[mid]:
            return binary_search(lis,mid+1,right,target)
        else:
            return binary_search(lis,left,mid-1,target)
    else:
        return -1
    
lis,target = input("Enter Element Separated By Space: ").split(),input("Enter Target Value: ")
res = binary_search(lis,0,len(lis),target)
print("{} Not Found.".format(target)) if res == -1 else print("{} Found At Index {}.".format(target,res))

#While Approach..................
def binary_search(lis,left,right,target):
    while left<=right:
        mid = (left+right)//2
        if target == lis[mid]:
            return mid
        elif target<lis[mid]:
            right = mid-1
        else:
            left = mid+1
    return -1

lis,target = input("Enter Element Separated By Space: ").split(),input("Enter Target Value: ")
res = binary_search(lis,0,len(lis),target)
print("{} Not Found.".format(target)) if res == -1 else print("{} Found At Index {}.".format(target,res))

'''
INPUT:
Enter Element Separated By Space: 34 5 23 546 23
Enter Target Value: 23
OUTPUT:
23 Found At Index 2.

INPUT:
Enter Element Separated By Space: 4 56 67 2 56 65
Enter Target Value: 2
OUTPUT:
2 Found At Index 3.

INPUT:
Enter Element Separated By Space: 67 98 23 9 98
Enter Target Value: 1
OUTPUT:
1 Not Found.
'''
