# Police Thief Grid Problem (Same Row Count)...................................................................................................................
size,zone = map(int,input().split())
grid = [list(map(str,input().split())) for _ in range(size)]
res = 0
for i in range(size):
    police,thief = -1,-1
    for j in range(size):
        if grid[i][j] == "P":
            police = j
        elif grid[i][j] == "T":
            thief = j
        if police>0 and thief>0:
            if abs(police-thief)<=zone:
                res+=1
print(res)
'''
INPUT:
3 1
N T P
N P T
N T P
OUTPUT:
3

INPUT:
4 2
N T N P
T N N P
N N P T
T T P P
OUTPUT:
4
'''
