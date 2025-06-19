# Sum Of Digits Into Single Digit And Printing Chr Of Odd Number And Number Of Even Number...........................................................
def single(num):
    if int(num)<10: return int(num)
    return int(single(sum([int(i) for i in str(num)])))
size = int(input())
lis = [print(chr(96+single(i)),end="") if single(i)%2 else print(single(i),end="") for i in input().split()]
'''
INPUT:
6
14 18 6 548 46 78
OUTPUT:
ei68a6

INPUT:
6
0 1 2 8 45 5896
OUTPUT:
0a28ia
'''
