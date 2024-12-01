#Left Right Number Triangle Pattern.....
size = int(input())
for i in range(size):
    for j in range(i+1):
        print(j+1,end=" ")
    print(str("  ")*(size-i-1)*2,end="")
    print((str(i+1)+(" "))*(i+1))
'''
INPUT - 4
OUTPUT
1             1
1 2         2 2
1 2 3     3 3 3
1 2 3 4 4 4 4 4
INPUT - 5
OUTPUT
1                 1
1 2             2 2
1 2 3         3 3 3
1 2 3 4     4 4 4 4
1 2 3 4 5 5 5 5 5 5
'''
