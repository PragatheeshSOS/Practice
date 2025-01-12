#Full Triangle Start And End By 1.........................
size = int(input())
print("** Printing the pattern... **")
for i in range(size):
    print((" ")*(size-i-1),end="")
    number = 1
    for j in range(i+1):
        print(number,end=" ")
        number = number*(i-j)//(j+1)
    print()
'''
INPUT:
4
OUTPUT:
** Printing the pattern... **
   1 
  1 1 
 1 2 1 
1 3 3 1 

INPUT:
3
OUTPUT:
** Printing the pattern... **
  1 
 1 1 
1 2 1 
'''
