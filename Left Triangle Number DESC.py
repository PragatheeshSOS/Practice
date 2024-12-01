#Left Triangle Number DESC.....
for i in range(int(input())):
    val = i+1
    for j in range(i+1):
        print(val,end=" ")
        val-=1
    print()
'''
INPUT - 5
OUTPUT
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
INPUT - 3
OUTPUT
1
2 1
3 2 1
INPUT - 8
OUTPUT
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
6 5 4 3 2 1
7 6 5 4 3 2 1
8 7 6 5 4 3 2 1
'''
