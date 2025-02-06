#Decimal To HexaDecimal........
def Dec2Hex(number):
    result = []
    while number>0:
        num = number%16
        if num>9:
            result.insert(0,chr(num+55))
        else:
            result.insert(0,num)
        number//=16
    return result
print(*Dec2Hex(int(input())),sep="")
'''
INPUT:
892
OUTPUT:
37C

INPUT:
564
OUTPUT:
234
'''
