# 1's and 2's Complement........................................
res = ""
for i in input():
    if i == "1":
        res += "0"
    else:
        res += "1"
print("1's complement is", res)
print("2's complement is", bin(int(res, 2) + 1)[2:].zfill(len(res)))
'''
INPUT:
1101
OUTPUT:
1's complement is 0010
2's complement is 0011

INPUT:
1
OUTPUT:
1's complement is 0
2's complement is 1

INPUT:
1111
OUTPUT:
1's complement is 0000
2's complement is 0001
'''
