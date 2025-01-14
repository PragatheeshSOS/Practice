# Matrix Rotation [Clockwise 90*].................
lis = eval(input())
size1,size2 = len(lis),len(lis[0])
for i in range(size1):
    for j in range(i,size1):
        lis[i][j],lis[j][i] = lis[j][i],lis[i][j]
for i in range(size1):
    m = lis[i].reverse()
print("[",end="")
for i in range(size1):
    print("[",end="")
    for j in range(size2):
        if size2-1!=j:
            print(lis[i][j],end=",")
        elif i != size1-1:
            print(lis[i][j],end="],")
        else:
            print(lis[size1-1][size2-1],end="]")
print("]")
'''
INPUT:
[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
OUTPUT:
[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

INPUT:
[[1,2,3],[4,5,6],[7,8,9]]
OUTPUT:
[[7,4,1],[8,5,2],[9,6,3]]
'''
'''
1 2 3        7 4 1
4 5 6   ->   8 5 2
7 8 9        9 6 3

5 1 9 11         15 13 2 5
2 4 8 10   ->    14 3 4 1
13 3 6 7         12 6 8 9
15 14 12 16      16 7 10 11
'''
