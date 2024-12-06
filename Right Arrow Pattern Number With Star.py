#Right Arrow Pattern Number With Star..........
lis,count = [],1
for i in range(int(input())):
    lis1 = []
    for j in range(i+1):
        if i!=j:
            printer = str(count)+"*"
        else:
            printer = str(count)
        count+=1
        print(printer,end="")
        lis1.append(printer)
    print()
    lis.append(lis1)
for i in lis[::-1]:
    print(*i,sep="")
'''
INPUT - 5
OUTPUT
1
2*3
4*5*6
7*8*9*10
11*12*13*14*15
11*12*13*14*15
7*8*9*10
4*5*6
2*3
1
INPUT - 7
OUTPUT
1
2*3
4*5*6
7*8*9*10
11*12*13*14*15
16*17*18*19*20*21
22*23*24*25*26*27*28
22*23*24*25*26*27*28
16*17*18*19*20*21
11*12*13*14*15
7*8*9*10
4*5*6
2*3
1
'''
