#Armstrong Number.....
def arm(num):
    length = len(str(num))
    lis = []
    for i in str(num):
        lis.append(int(i)**length)
    return num == sum(lis)
print("Armstrong Number") if arm(int(input())) else print("Not a Armstrong")
'''
INPUT - 153
OUTPUT - Armstrong Number
INPUT - 100
OUTPUT - Not a Armstrong
INPUT - 1634
OUTPUT - Armstrong Number
'''
