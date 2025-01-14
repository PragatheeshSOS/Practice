#Reverse Spiral Matrix Anti-Clockwise [DRUL]...................
#Starts From Top To Down. Down To Right. Right To Up. Up To Left.
size1, size2 = int(input()), int(input())
lis = [list(map(int, input().split())) for _ in range(size1)]
top,bottom,left,right,count=0,size1-1,0,size2-1,size1*size2
while count>0:
    for i in range(top,bottom+1):
        if count>0:
            print(lis[i][left],end=" ")
            count-=1
    left+=1
    for i in range(left,right+1):
        if count>0:
            print(lis[bottom][i],end=" ")
            count-=1
    bottom-=1
    for i in range(bottom,top-1,-1):
        if count>0:
            print(lis[i][right],end=" ")
            count-=1
    right-=1
    for i in range(right,left-1,-1):
        if count>0:
            print(lis[top][i],end=" ")
            count-=1
    top+=1
'''
INPUT:
4
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
OUTPUT:
1 5 9 13 14 15 16 12 8 4 3 2 6 10 11 7

INPUT:
4
3
11 2 3
51 6 7
9 100 11
13 14 15
OUTPUT:
11 51 9 13 14 15 11 7 3 2 6 100
'''
