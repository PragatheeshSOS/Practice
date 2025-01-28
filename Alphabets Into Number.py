#Alphabets Into Number..........
#Approach 1...............
number = input()
result = 0
for i, char in enumerate(number):
    result = result * 26 + (ord(char) - ord('A') + 1)
print(result)
#Approach 2...............
number,res = input(),0
for i in range(len(number)):
    if i == 0:
        res+=(ord(number[i])-ord('A')+1)
    else:
        res*=26
        res+=(ord(number[i])-ord('A')+1)
print(res)
'''
INPUT:
B
OUTPUT:
2

INPUT:
AB
OUTPUT:
28

INPUT:
ZL
OUTPUT:
688
'''
