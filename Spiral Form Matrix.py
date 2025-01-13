#Spiral Form Matrix..........
size1,size2 = map(int,input().split())
lis = [list(map(int,input().split())) for _ in range(size1)]
count,top,right,bottom,left = size1*size2,0,size2-1,size1-1,0
while(count>0):
    for i in range(bottom+1):
        if count!=0:
            print(lis[top][i],end=" ")
            count-=1
    top+=1
    for i in range(top,bottom+1):
        if count!=0:
            print(lis[i][right],end=" ")
            count-=1
    right-=1
    for i in range(right,-1,-1):
        if count!=0:
            print(lis[bottom][i],end=" ")
            count-=1
    bottom-=1
    for i in range(bottom,top,-1):
        if count!=0:
            print(lis[i][left],end=" ")
            count-=1
    left+=1
'''
INPUT:
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
OUTPUT:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
'''

# Inefficient Code....................
m,n = map(int,input().split())
t,a,f,b = [],0,0,0
v=m*n
q=-1

for i in range(n):
    t.append(list(map(int,input().split())))
    
while(a!=2):
    if f !=1:
        for j in range(n):
            q+=1
            if(q==v):
                break
            print(t[0][j],end=" ")
            f = 1
        b = j
    else:
        for j in range(1,n):
            q+=1
            if(q==v):
                break
            print(t[j][b],end=" ")
    a+=1
    
a,f = 0,0
while(a!=2):
    if f!=1:
        for j in range(b-1,0,-1):
            q+=1
            if(q==v):
                break
            print(t[b][j],end=" ")
            f = 1
        b = j-1
    else:
        for j in range(n-1,0,-1):
            q+=1
            if(q==v):
                break
            print(t[j][b],end=" ")
        b = j
    a+=1

a,f = 0,0
while(a!=2):
    if f!=1:
        for j in range(b,n-1):
            q+=1
            if(q==v):
                break
            print(t[b][j],end=" ")
        f = 1
        b = j
    else:
        for j in range(b,0,-1):
            q+=1
            if(q==v):
                break
            print(t[b][j],end=" ")
    a+=1
