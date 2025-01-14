#Spiral Form Matrix..........
size1,size2 = int(input()),int(input())
lis = [list(map(int, input().split())) for _ in range(size1)]
count,top,right,bottom,left = size1*size2,0,size2-1,size1-1,0
while count>0:
    for i in range(left,right+1):
        if count>0:
            print(lis[top][i],end=" ")
            count-=1
    top+=1
    for i in range(top,bottom+1):
        if count>0:
            print(lis[i][right],end=" ")
            count-=1
    right-=1
    for i in range(right,left-1,-1):
        if count>0:
            print(lis[bottom][i],end=" ")
            count-=1
    bottom-=1
    for i in range(bottom,top-1,-1):
        if count>0:
            print(lis[i][left],end=" ")
            count-=1
    left+=1
'''
INPUT:
4
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
OUTPUT:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

INPUT:
3
6
1 2 3 4 5 6
7 8 9 10 11 12
13 14 15 16 17 18
OUTPUT:
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11 
'''
