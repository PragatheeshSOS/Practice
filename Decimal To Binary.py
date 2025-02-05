#Decimal To Binary....
def DeBi(number):
    result = []
    while(number>0):
        result.insert(0,number%2)
        number//=2
    return result
number = int(input())
print(*DeBi(number),sep="")
'''
INPUT:
10
OUTPUT:
1010

INPUT:
20
OUTPUT:
10100

INPUT:
13
OUTPUT:
1101
'''
