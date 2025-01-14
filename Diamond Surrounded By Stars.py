#Diamond Surrounded By Stars..............
size,lis = int(input()),[]
for i in range(size):
    stars = (str("*")*(size-i))+(str(" ")*(((i+1)*2)-1))+(str("*")*(size-i))
    print(stars)
    lis.append(stars)
for i in lis[::-1]:
    print(*i,sep="")
'''
INPUT:
5
OUTPUT:
***** *****
****   ****
***     ***
**       **
*         *
*         *
**       **
***     ***
****   ****
***** *****

INPUT:
4
OUTPUT:
**** ****
***   ***
**     **
*       *
*       *
**     **
***   ***
**** ****
'''
