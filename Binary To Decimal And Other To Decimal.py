def binary_to_decimal(number):
    i = 0
    while number!=0:
        digit = number%10
        decimal+=digit*(2**i) # Here, 2 Is Replaced With Required Number (i.e) 8,16..
        num//=10
        i+=1
    return decimal
print(binary_to_decimal(int(input())))
'''
INPUT:
10
OUTPUT:
2
'''
