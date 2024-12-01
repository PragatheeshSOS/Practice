#Largest Prime......
def isprime(num):
    if num<2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
for i in range(int(input()),2,-1):
    if isprime(i) == True:
        print(i,end="")
        exit(0)
'''
INPUT - 15
OUTPUT - 13
INPUT - 30
OUTPUT - 29
'''
