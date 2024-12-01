#Right Triangle Pattern Number Of i......
size = int(input())
for i in range(size):
    print(str(" ")*(size-i-1)*2,(str(i+1)+(" "))*(i+1),sep="")
'''
INPUT - 3
OUTPUT
    1
  2 2
3 3 3
INPUT - 4
OUTPUT
      1
    2 2
  3 3 3
4 4 4 4
'''
