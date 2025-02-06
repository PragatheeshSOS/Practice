# Decimal To Octal......
#Approach 1.................
def Dec2Oct(number):
    result = []
    while number>0:
        result.insert(0,number%8)
        number//=8
    return result
print(*Dec2Oct(int(input())),sep="")

#Approach 2.................
def Dec2Oct(number):
    result,power = 0,1
    while number>0:
        result+=(number%8)*power
        number//=8
        power*=10
    return result
print(Dec2Oct(int(input())))
'''
INPUT:
148
OUTPUT:
224

INPUT:
199
OUTPUT:
307
'''
