#Right Arrow Pattern Numbers......
lis = []
for i in range(1,int(input())+1):
    arr = []
    for j in range(1,i+1):
        print(j,end=" ")
        arr.append(j)
    lis.append(arr)
    print()
for i in range(len(lis)-1,-1,-1):
    print(*lis[i])
'''
INPUT - 3
OUTPUT
1 
1 2 
1 2 3
1 2 3
1 2
1
INPUT - 4
OUTPUT
1 
1 2 
1 2 3 
1 2 3 4
1 2 3 4
1 2 3
1 2
1
'''
