# Updown Triangle (Full Star As X).....................................
size = int(input())
for i in range(size,0,-1):
    print(str(" ")*(size-i),str("* ")*i,sep="")
for i in range(1,size+1):
    print(str(" ")*(size-i),str("* ")*i,sep="")
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
