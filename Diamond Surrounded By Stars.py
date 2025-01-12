#Diamond Surrounded By Stars..............
size,lis = int(input()),[]
for i in range(size):
    string = ""
    for j in range(size):
        if j <= size-i-1:
            string+="*"
        else:
            string+=" "
    res = string+" "+string[::-1]
    print(res)
    lis.append(res)
for i in lis[::-1]:
    print(i)
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
