#Printing Equal Positive And Negative Numbers.....
size = int(input())
for i in range(size//2,0,-1):
    print(i,end=" ")
for i in range(1,(size//2)+1):
    print(f"-{i}",end=" ")
'''
INPUT - 6
OUTPUT - 3 2 1 -1 -2 -3
INPUT - 10
OUTPUT - 5 4 3 2 1 -1 -2 -3 -4 -5
INPUT - 8
OUTPUT - 4 3 2 1 -1 -2 -3 -4
INPUT - 20
OUTPUT - 10 9 8 7 6 5 4 3 2 1 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
'''
