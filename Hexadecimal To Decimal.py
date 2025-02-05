#Hexadecimal To Decimal.....
def hexd(number):
    result,power = 0,0
    for i in range(len(number)-1,-1,-1):
        if '0'<=number[i]<='9':
            result+=(ord(number[i])-48)*(16**power)
        elif 'A'<=number[i]<='F':
            result+=(ord(number[i])-55)*(16**power) # Subracting 55 To Make A = 10.
        power+=1
    return result
print(hexd(input()))
'''
INPUT:
1AF
OUTPUT:
431
'''
