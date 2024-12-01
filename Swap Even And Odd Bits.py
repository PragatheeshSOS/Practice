#Swap Even And Odd Bits......
number = int(input())
print(((number & 0xAAAAAAAA) >> 1) | ((number & 0x55555555) << 1))
'''
INPUT - 14
OUTPUT - 13
INPUT - 10
OUTPUT - 5
'''
