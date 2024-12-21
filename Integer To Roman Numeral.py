#Integer To Roman Numeral - L3P3.
n = int(input())
d={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',90:'XC',40:'XL',4:'IV',9:'IX',900:'CM',400:'CD'}
l = list(d.keys())
l.sort(reverse=True)
print("Roman:",end=" ")
while(n>0):
    for i in l:
        if n//i>=1:
            print((d[i])*(n//i),end="")
            n=n%i
'''
INPUT:
45

OUTPUT:
Roman: XLV

INPUT:
7

OUTPUT:
Roman: VII

INPUT:
532

OUTPUT:
Roman: DXXXII
'''
