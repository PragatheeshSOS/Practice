#Merge Sort...........
'''
Time Complexity = O(n log(n))
Space Complexity = O(n)
'''
def meregeSort(lis):
    if len(lis)<=1:
        return lis
    mid = len(lis)//2
    left,right = meregeSort(lis[:mid]),meregeSort(lis[mid:])
    print("M->   ",left,right)
    return merge(left,right)

def merge(left,right):
    res,i,j = [],0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    print("res-> ",res)
    return res

print(*meregeSort(list(map(int,input().split()))))

'''
INPUT:
56 34 12 65 45 65 16 84 8
OUTPUT:
8 12 16 34 45 56 65 65 84

ADDITONAL VIEW:
56 34 12 65 45 65 16 84 8
M->    [56] [34]
res->  [34, 56]
M->    [12] [65]
res->  [12, 65]
M->    [34, 56] [12, 65]
res->  [12, 34, 56, 65]
M->    [45] [65]
res->  [45, 65]
M->    [84] [8]
res->  [8, 84]
M->    [16] [8, 84]
res->  [8, 16, 84]
M->    [45, 65] [8, 16, 84]
res->  [8, 16, 45, 65, 84]
M->    [12, 34, 56, 65] [8, 16, 45, 65, 84]
res->  [8, 12, 16, 34, 45, 56, 65, 65, 84]
8 12 16 34 45 56 65 65 84
'''
