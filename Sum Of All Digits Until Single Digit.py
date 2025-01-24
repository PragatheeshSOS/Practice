#Sum Of All Digits Until Single Digit......
number = int(input())
while(number>0):
    if number<10:
        print(number)
        exit(0)
    else:
        res = number
        fin = 0
        while(res>0):
            fin+=(res%10)
            res//=10
        number = fin
'''
INPUT:
1234
OUTPUT:
1

INPUT:
273
OUTPUT:
3
'''
