# Diamond Star Border Pattern....................................................
size = int(input())
for i in range(size-1):
    for j in range(2*size-1):
        print("*" if i+j == size-1 or j == size-1+i else " ",end="")
    print()
for i in range(size-1,-1,-1):
    for j in range(2*size-2,-1,-1):
        print("*" if i+j == size-1 or j == size-1+i else " ",end="")
    print()
'''
INPUT:
4
OUTPUT:
   *   
  * *  
 *   * 
*     *
 *   * 
  * *  
   *   
INPUT:
7
OUTPUT:
      *      
     * *     
    *   *    
   *     *   
  *       *  
 *         * 
*           *
 *         * 
  *       *  
   *     *   
    *   *    
     * *     
      *      
'''
