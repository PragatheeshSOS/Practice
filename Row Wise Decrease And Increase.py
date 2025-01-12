#Row Wise Decrease And Increase..........
size = int(input())
print("Value of N:",size)
for i in range(size):
    lis = []
    for j in range(size):
        if i<=j:
            print(size-i,end="")
            lis.append(size-i)
        else:
            print(size-j,end="")
            lis.append(size-j)
    print(*lis[-2::-1],sep="")
'''
INPUT:
4
OUTPUT:
Value of N: 4
4444444
4333334
4322234
4321234

INPUT:
7
OUTPUT:
Value of N: 7
7777777777777
7666666666667
7655555555567
7654444444567
7654333334567
7654322234567
7654321234567
'''
