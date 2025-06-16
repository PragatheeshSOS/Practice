# Up And Down Triangle (Inverted Triangle Up And Triangle Down)........................................
size = int(input())
for i in range(size):
    for j in range(size):
        if i>j:
            print(" ",end="")
        else:
            print("* ",end="")
    print() if i <size-1 else None
for i in range(size+1):
    for j in range(size):
        if i<size-j:
            print(" ",end="")
        else:
            print("* ",end="")
    print()
'''
INPUT:
5
OUTPUT:
* * * * * 
 * * * * 
  * * * 
   * * 
    *      
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
