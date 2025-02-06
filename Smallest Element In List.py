#Smallest Element In List.........
import math
def secondSmall(lis):
    first = second = math.inf
    if len(lis)<2:
        return "Size is smaller than expected."
    for i in lis:
        if i<first:
            second = first
            first = i
        elif i<second and i!=first:
            second = i
    if second == math.inf:
        return "No Smallest Element Is Found."
    else:
        return f"Second Smallest Element Is {second}."
print(secondSmall(list(map(int,input().split()))))
'''
INPUT:
1 1
OUTPUT:
No Smallest Element Is Found.

INPUT:
1
OUTPUT:
Size is smaller than expected.

INPUT:
2 6 5 3 7
OUTPUT:
Second Smallest Element Is 3.
'''
