# Square Number Inside Decreasing And Then Increasing Pattern............
size = int(input())
print("Value of N:",size)
for i in range(size,0,-1):
    for j in range(size,0,-1):
        if i>=j:
            print(i,end="")
        else:
            print(j,end="")
    for j in range(2,size+1):
        if i>=j:
            print(i,end="")
        else:
            print(j,end="")
    print()
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
