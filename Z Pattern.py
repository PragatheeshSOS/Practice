# Z Pattern....
size = int(input())
for i in range(size):
    for j in range(size):
        # if i == 0 or i == size-1 or j == size-i-1:
        #     print("*",end="")
        # else:
        #     print(" ",end="")
        print("*",end=" ") if i == 0 or j == size-1 or j == size-i-1 else print(" ",end=" ")
    print()
'''
INPUT - 10
OUTPUT
* * * * * * * * * * 
                *   
              *     
            *       
          *         
        *           
      *             
    *               
  *                 
* * * * * * * * * *
INPUT - 3
OUTPUT
* * *
  *  
* * *
'''
