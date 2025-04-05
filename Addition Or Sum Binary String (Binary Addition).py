![Alt txt] (https://github.com/user-attachments/assets/321ce069-48ba-4f94-84f4-73e152d7c719)
# Manual Sum Of Binary String.......
number1,number2 = input(),input()
number1,number2 = number1.zfill(max(len(number1),len(number2))),number2.zfill(max(len(number1),len(number2)))
carry,res = 0,[]
for i in range(len(number1)-1,-1,-1):
    number = int(number1[i])+int(number2[i])+carry
    res.insert(0,number%2)
    carry = number//2
if carry>0:
    res.insert(0,1)
print(*res,sep="")

# Sum Of Binary String Using Inbuild Function.......
print(bin(int(input(),2)+int(input(),2))[2::])

'''
INPUT:
11
1
OUTPUT:
100

INPUT:
1010
1011
OUTPUT:
10101
'''
