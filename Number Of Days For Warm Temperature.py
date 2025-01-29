#Number Of Days For Warm Temperature..................
temp,stack = [int(input()) for _ in range(int(input()))],[]
res = [0]*len(temp)
for i in range(len(temp)):
    while stack and temp[stack[-1]]<temp[i]:
        prev = stack.pop()
        res[prev] = i-prev
    stack.append(i)
print(*res,sep=",")
'''
INPUT:
8
73
74
75
71
69
72
76
73
OUTPUT:
1,1,4,2,1,1,0,0

INPUT:
3
30
60
90
OUTPUT:
1,1,0
'''
