#Matrix's Determinant..............
import numpy as np
size1,size2 = int(input()),int(input())
print(f"Determinant of the matrix ={int(round(np.linalg.det(np.array([list(map(int,input().split())) for _ in range(size1)]))))}")
'''
INPUT:
2
2
1 2
3 4
OUTPUT:
Determinant of the matrix =-2

INPUT:
3
3
2 1 3
1 0 2
2 0 -2
OUTPUT:
Determinant of the matrix =6
'''
