#Counting Distinct Element In Array (Unqiue Elements In Array)..............
#Approach 1....................
lis = list(map(int,input().split()))
checker,count = [False]*len(lis),0
for i in range(len(lis)):
    if not checker[i]:
        for j in range(i+1,len(lis)):
            if lis[i] == lis[j]:
                checker[j] = True
        count+=1
print(count)
'''
Time Complexity = O(n**2)
Space Complexity = O(n)
'''

#Approach 2......................
print(len(set(list(map(int, input().split())))))
'''
Time Complexity = O(n)
Space Complexity = O(n)
'''

#Approach 3......................
def unq(lis):
    count = 0
    for i in range(len(lis)):
        flag = False
        for j in range(i+1,len(lis)):
            if lis[i] == lis[j]:
                flag = True
                break
        if flag == False:
            count+=1
    return count

print(unq(list(map(int,input().split()))))
'''
Time Complexity = O(n**2)
Space Complexity = O(1)
'''

#Approach 4..........
def unq(lis):
    lis.sort()
    count,i = 0,0
    while i<len(lis):
        while i<len(lis)-1 and lis[i] == lis[i+1]:
            i+=1
        count+=1
        i+=1
    return count

print(unq(list(map(int,input().split()))))
'''
Time Complexity = O(n log(n))
Space Complexity = O(1)
'''
'''
INPUT:
1 2 4 5 4 2
OUTPUT:
4

INPUT:
1 2 4 5 6
OUTPUT:
5

INPUT:
1 5 5 4 5
OUTPUT:
3
'''
