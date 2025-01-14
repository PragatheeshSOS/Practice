# Last Two Digit Of Nth Fibonacci....................
def fib(num):
    if num<2:
        return num
    else:
        return lis[-1]+lis[-2]
lis = []
for i in range(int(input())+1):
    lis.append(fib(i))
res = lis[-1]%100
if res<10:
    print(f"0{res}")
else:
    print(res)
'''
INPUT:
13
OUTPUT:
33

INPUT:
12
OUTPUT:
44

INPUT:
6
OUTPUT:
08
'''
