#Fibonacci Series......
def fib(n):
  if n<2:
    return n
  else:
    return lis[-1]+lis[-2]
given,lis = int(input()),[]
for i in range(given):
  lis.append(fib(i))
print(*lis)
'''
INPUT - 5
OUTPUT - 0 1 1 2 3
INPUT - 7
OUTPUT - 0 1 1 2 3 5 8
'''
