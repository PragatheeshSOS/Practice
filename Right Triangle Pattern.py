#Right Triangle Pattern......
size = int(input())
for i in range(size+1):
    for j in range(size-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()
'''
INPUT - 6
OUTPUT
      *
     **
    ***
   ****
  *****
 ******
*******
INPUT - 4
OUTPUT
    *
   **
  ***
 ****
*****
'''
