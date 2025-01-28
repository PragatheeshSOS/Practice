#X Pattern..............
#Approach 1....................
size,lis = int(input()),[]
for i in range(size):
    string = ""
    for j in range(size):
        if i == j:
            string+="*"
        else:
            string+=" "
    res = string + string[-2::-1]
    print(res)
    lis.append(res)
for i in lis[-2::-1]:
    print(i)
#Approach 2..............
size,res = int(input()),[]
for i in range(size):
    lis1 = []
    for j in range(size*2):
        if i == j or j == (size*2)-i-2:
            print("*",end="")
            lis1.append("*")
        else:
            print(" ",end="")
            lis1.append(" ")
    res.append(lis1)
    print()
[print(*i,sep="") for i in res[-2::-1]]
'''
INPUT:
3
OUTPUT:
*   *
 * * 
  *  
 * * 
*   *

INPUT:
6
OUTPUT:
*         *
 *       * 
  *     *  
   *   *   
    * *    
     *     
    * *    
   *   *   
  *     *  
 *       * 
*         *
'''
