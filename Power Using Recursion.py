#Power Using Recursion..............
def power(x,n):
    if n!=0:
        num = x*power(x,n-1)
        # print("i-> ",x,num)
        return num
    else:
        # print("i-> ",x,1)
        return 1
print(power(int(input("Enter Value x: ")),int(input("Enter Value n: "))))
'''
INPUT:
Enter Value x: 4
Enter Value n: 3
OUTPUT:
64

INPUT:
Enter Value x: 5
Enter Value n: 3
OUTPUT:
125

INPUT:
Enter Value x: 2
Enter Value n: 4
OUTPUT:
16
'''
