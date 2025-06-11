# Two Sum Solution.............................
lis = [int(input()) for _ in range(int(input()))]
target = int(input())
left,right = 0,len(lis)-1
while left<right:
    if lis[right]>=target:
        right-=1
    elif lis[left]+lis[right] == target:
        print(f"Index1: {left}\nIndex2: {right}")
        exit()
    left+=1
print("No two sum solution")
'''
Input         Expected
4             Index1: 1
2             Index2: 3
6
11
3
9

5             No two sum solution
1
2
3
4
5
10
'''
