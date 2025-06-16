#Matrix's Determinant..............
import numpy as np
size1,size2 = int(input()),int(input())
print(f"Determinant of the matrix ={int(round(np.linalg.det(np.array([list(map(int,input().split())) for _ in range(size1)]))))}")

# Approach 2.................................
size1,size2 = int(input()),int(input())
if size1 == size2 == 2:
    one,two = map(int,input().split())
    three,four = map(int,input().split())
    print(f"Determinant of the matrix ={(one*four)-(two*three)}")
else:
    a,b,c = map(int,input().split())
    d,e,f = map(int,input().split())
    g,h,i = map(int,input().split())
    print(f"Determinant of the matrix ={(a*((e*i)-(f*h)))-(b*((d*i)-(f*g)))+(c*((d*h)-(e*g)))}")
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
