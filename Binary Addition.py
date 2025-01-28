#Binary Addition......... (This Approach Only Works)
num1,num2 = bin(int(input(),2))[2:],bin(int(input(),2))[2:]
maxi = max(len(num1),len(num2))
num1,num2,carry,res = num1.zfill(maxi)[::-1],num2.zfill(maxi)[::-1],0,[]
for i, j in zip(num1,num2):
    sum = int(i)+int(j)+carry
    res.append(sum%2)
    carry = sum//2
if carry:
    res.append(carry)
print(*res[::-1],sep="")
'''
INPUT:
100
101

OUTPUT:
1001
'''
