#Frequency Of the Elements(Elements Count)..............
#Approach 1...........
lis = list(map(int,input().split()))
checker,count = [False]*len(lis),1
for i in range(len(lis)):
    if not checker[i]:
        count = 1
        for j in range(i+1,len(lis)):
            if lis[i] == lis[j]:
                checker[j] = True
                count+=1
        print(lis[i],"->",count)
'''
Time Complexity = O(n**2)
Space Complexity = O(n)
'''

#Approach 2...........
lis = list(map(int,input().split()))
for i in range(len(lis)):
    flag,count = False,0
    for j in range(i+1,len(lis)):
        if lis[i] == lis[j]:
            flag = True
            break
    if flag == True:
        continue
    for j in range(i+1):
        if lis[i] == lis[j]:
            count+=1
    print(lis[i],"->",count)
'''
Time Complexity = O(n**2)
Space Complexity = O(n)
'''

#Approach 3.............
lis = list(map(int,input().split()))
lis.sort()
i = 0
while i<len(lis):
    count = 1
    while i<len(lis)-1 and lis[i] == lis[i+1]:
        i+=1
        count+=1
    print(lis[i],"->",count)
    i+=1
'''
Time Complexity = O(n log(n))
Space Complexity = O(n)
'''

#Approach 4..............
lis = list(map(int,input().split()))
for i in frozenset(lis):
    print(i,"->",lis.count(i))
'''
Time Complexity = O(k.n) (Worst Case = O(n**2))
Space Complexity = O(n+k) (Worst Case = O(n))
'''

#Approach 5..............
from collections import defaultdict
lis = list(map(int, input().split()))
frequency = defaultdict(int)
for num in lis:
    frequency[num] += 1
for num, count in frequency.items():
    print(num, "->", count)
'''
Time Complexity = O(n)
Space Complexity = O(n)
'''
'''
INPUT:
1 3 4 1 3
OUTPUT:
1 -> 2
3 -> 2
4 -> 1

INPUT:
1 3 1 1 3 1 2 1 3
OUTPUT:
1 -> 5
3 -> 3
2 -> 1
'''
