#Sparse Matrix Or Not................
size1,size2 = map(int,input().split())
count = 0
for i in range(size1):
    for j in input().split():
        if int(j) == 0:
            count+=1
print("The given matrix is Sparse matrix") if (size1*size2)//2 <= count else print("The given matrix is not a Sparse matrix")
'''
INPUT:
3 3
1 0 3
0 0 4
6 0 0
OUTPUT:
The given matrix is Sparse matrix

INPUT:
3 3
1 0 3
7 0 8
6 0 6
OUTPUT:
The given matrix is not a Sparse matrix
'''
