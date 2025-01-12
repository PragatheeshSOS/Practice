#X Pattern..............
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
