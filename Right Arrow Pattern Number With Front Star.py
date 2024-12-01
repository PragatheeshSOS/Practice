#Right Arrow Pattern Number With Front Star......
lis = []
for i in range(int(input())):
    lis1 = []
    for j in range(i+1):
        if j == 0:
            print(j+1,end=" ")
            lis1.append(j+1)
        else:
            printer = "*"+str(j+1)
            print(printer,end=" ")
            lis1.append(printer)
    lis.append(lis1)
    print()
for i in range(len(lis)-1,-1,-1):
    print(*lis[i])
'''
INPUT - 3
OUTPUT
1 
1 *2 
1 *2 *3 
1 *2 *3
1 *2
1
INPUT - 2
OUTPUT
1 
1 *2 
1 *2
1
'''
