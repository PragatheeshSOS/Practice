# Rat In A Maze (Down-Right | 2 Directional Grid | Backtracting)................................................................

# Verifying Path Available Or Not.
def isway(row,col):
    return row<size and col<size and lis[row][col] == 0
    
# Solution Function (Recurtion/Backtracking).
def ans(row,col):
    res[row][col] = 1
    if row == size-1 and col == size-1:   # Verifies Destination Reached.
        return True
    if isway(row+1,col) and ans(row+1,col):    # Row-wise Iteration.
        return True
    if isway(row,col+1) and ans(row,col+1):    # Column-wise Iteration.
        return True
    res[row][col] = 0       # Reassigning 0 If No Path Found.
    return False

# Inputs.    
size = int(input())
lis = [list(map(int,input().split())) for _ in range(size)]

# Resulting Grid.
res = [[0]*size for _ in range(size)]

# Output.
[print(*i) for i in res] if isway(0,0) and ans(0,0) else print("No solution exists")

'''
-----------------------------------------------
INPUT        |    EXPECTED
-----------------------------------------------
5                 No solution exists
1 0 1 0 1
1 1 1 1 1
0 0 0 0 0
0 0 0 0 1
1 0 0 0 0
-----------------------------------------------
INPUT        |    EXPECTED
-----------------------------------------------
5
0 0 1 1 1         1 1 0 0 0
1 0 0 1 1         0 1 1 0 0
1 1 0 0 1         0 0 1 1 0
1 0 1 0 1         0 0 0 1 0
1 0 1 0 0         0 0 0 1 1
'''
