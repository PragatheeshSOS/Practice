#Diamond Pattern...........
size,printer,lis = int(input()),input(),[]
for i in range(size):
    value = (str(" ")*(size-i-1)+printer*(((i+1)*2)-1))
    print(value)
    lis.append(value)
lis.pop()
[print(i) for i in lis[::-1]]
'''
INPUT:
3
a
OUTPUT:
  a
 aaa
aaaaa
 aaa
  a

INPUT:
6
X
OUTPUT:
     X
    XXX
   XXXXX
  XXXXXXX
 XXXXXXXXX
XXXXXXXXXXX
 XXXXXXXXX
  XXXXXXX
   XXXXX
    XXX
     X
'''
