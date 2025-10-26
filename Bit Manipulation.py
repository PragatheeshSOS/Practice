# Example Input - 13 5 7
# AND Operations
print(int(input())&int(input())&int(input()))

# OR Operations
print(int(input())|int(input())|int(input()))

# XOR Operations
print(int(input())^int(input())^int(input())) # Do XOR First Two And Follow In Set Order

# Example Input - 13 2,13 3
# Left Shift Operations x*(2**n) n - bit value (2**(number))
print(int(input())<<int(input()))

#Right Shift Operations x*(1//2**n) n - bit value (2**(number))
print(int(input())>>int(input()))

# NOT Operations if input(+) answer = -(input()+1) eg:10 = -11 or input(-) answer = input()-1 eg -10 9
print(~(int(input())))

#Unqiue Number (XOR)
def un(x):
    ans = 0
    for num in x:
        ans = ans^num
    return ans
lis = [-1,0,1,9,-2,11,0,1,-2,9,11]
print(un(lis))

#Number Is Odd Or Even (Slower Compared To %)
print("odd") if int(input())&1 == 1 else print("even")

#Extract Or Find Nth Bit. eg: 13 1 - 0, 13 2 - 0
print(1) if (int(input())&(1<<int(input())))>10 else print(0) #OneLineCode.
def findbit(num,ele):
    mask = 1<<ele
    num = num&mask
    if (num>0):
        return 1
    else:
        return 0
print(findbit(13,1))
print(findbit(13,2))

#Set A Bit. eg: 13 1 - 15, 27 2 - 31.
print(int(input())|(1<<int(input()))) #OneLineCode.
def setbit(num,ele):
    mask = 1<<ele
    num = num|mask
    return num
print(setbit(13,1))
print(setbit(27,2))

#Clear Or Change Nth Bit. eg: 13 2 - 9.
print(int(input())&(~(1<<int(input())))) #OneLineCode.
def changebit(num,ele):
    mask = ~(1<<ele)
    num = num&mask
    return num
print(changebit(13,2))

#Set Or Reset Bit. (Whole 1 And 0 Are Opposited) eg: 13 1 1 - 15, 13 2 0 - 9
def resetbit(num,ele,val):
    mask = ~(1<<ele)
    res = num&mask
    mask2 = val<<ele
    res = res|mask2
    return res
print(resetbit(13,1,1))
print(resetbit(13,2,0))

#ClearLast Bit. Execpt Last Bit All Are Opposed. eg: 13 3 - 8.
print(int(input())&(-1<<int(input()))) #OneLineCode.
def clearbit(num,ele):
    mask = (~0)<<ele # (-1)<<ele. alt aprch.
    num&=mask
    return num
print(clearbit(13,3))

#SetLast Bit. eg: 178 3 - 183.
print(int(input())|((1<<int(input()))-1))
def setLast(num,ele):
    mask = (1<<ele)-1
    ans = num|mask
    return ans
print(setLast(178,3))

#Set i to j Bits. (Frm _ To 1).
def ijsetbits(num,i,j):
    N = j-i+1
    mask = (1<<N)-1
    mask = mask<<i
    ans = mask|num
    return ans
print(ijsetbits(171,2,4))

#Check Number Is Power Of Two.
num = 2
print("Yes") if num&(num-1) == 0 else print("No") #OneLineCode
def CheckPow2(num):
    if num&(num-1) == 0:
        print("Yes")
    else:
        print("No")
CheckPow2(2)
CheckPow2(34)

#Replace "num" By M from i to j bits.
def replace(num,m,i,j):
    mask1 = (-1)<<(j+1)
    mask2 = (1<<i)-1
    mask = mask1|mask2
    ans = num&mask
    m = m<<i
    num = ans|m
    return num
print(replace(73,5,2,4)) #OUTPUT - 85
print(replace(73,3,2,4)) #OUTPUT - 77

#Number Of Bit Counts.
def countbits(num):
    count = 0
    while(num>0):
        num>>=1
        count+=1
    return count
print(countbits(1701)) #OUTPUT - 11

#Reset/Clear First i Bits.
def clearfirstibits(num,i):
    number,count = num,0
    while(num>0):
        num>>=1
        count+=1
    return ((1<<(count-i))-1)&number
print(clearfirstibits(171,4)) #OUTPUT - 11
print(clearfirstibits(171,2)) #OUTPUT - 43

#Set/Change First i Bits To 1.
def setfirstibits(num,i):
    number,count = num,0
    while(num>0):
        num>>=1
        count+=1
    return (((1<<i)-1)<<(count-i))|number
print(setfirstibits(171,4)) #OUTPUT - 251
print(setfirstibits(171,2)) #OUTPUT - 235

#Count Number Of Set Bits.
#Method - 1.
def countsetbits(num):
    count = 0
    while(num>0):
        if num&1 == 1:
            count+=1
        num>>=1
    return count
print(countsetbits(171)) #OUTPUT - 5
print(countsetbits(14422)) #OUTPUT - 7

#Method -2.
import math
print(math.ceil(math.log(14422,2)))
