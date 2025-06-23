# Max Of Sum Of Triplets (a<b<c)..................................................................................
lis = [int(input()) for _ in range(int(input()))]
res = []
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        for k in range(j+1,len(lis)):
            if lis[i]<lis[j] and lis[j]<lis[k]:
                res.append(lis[i]+lis[j]+lis[k])
print(max(res) if res else 0)
'''
INPUT:	
6
2
5
3
1
4
9
OUTPUT:
16
'''
