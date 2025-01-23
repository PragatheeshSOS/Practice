#Matrix Addition And Subtraction......
size1,size2 = map(int,input().split())
size11,size22 = map(int,input().split())
if size1<0 or size2<0 or size11<0 or size22<0:
    print("Row and column size should not be negative")
elif size1 != size11 and size2 != size22:
    print("Row and column size should be same for 2 matrices")
else:
    matrix1 = [list(map(int,input().split())) for _ in range(size1)]
    matrix2 = [list(map(int,input().split())) for _ in range(size11)]
    print("Addition:")
    [print(matrix1[i][j]+matrix2[i][j]) for i in range(size1) for j in range(size11)]
    print("Subtraction:")
    [print(matrix1[i][j]-matrix2[i][j]) for i in range(size1) for j in range(size11)]
'''
INPUT:
2 2
2 2
1 2
3 4
4 5
6 7
OUTPUT:
Addition:
5
7
9
11
Subtraction:
-3
-3
-3
-3

INPUT:
-2 -2
-2 -2
OUTPUT:
Row and column size should not be negative

INPUT:
3 4
1 2
OUTPUT:
Row and column size should be same for 2 matrices
'''
