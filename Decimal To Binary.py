#Decimal To Binary....
#Approach 1..........
def DeBi(number):
    result = []
    while(number>0):
        result.insert(0,number%2)
        number//=2
    return result
print(*DeBi(int(input())),sep="")

#Approach 2...........
def d2b(number):
    result,power = 0,1
    while(number>0):
        result+=(number%2)*power
        number//=2
        power*=10
    return result
print(d2b(int(input())))
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
