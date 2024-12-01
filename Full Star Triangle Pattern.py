#Full Star Triangle Pattern.....
size = int(input())
for i in range(1,size+1):
    print(str(" ")*(size-i),str("* ")*i,sep="")
'''
INPUT - 5
OUTPUT
    * 
   * * 
  * * * 
 * * * * 
* * * * *
INPUT - 7
OUTPUT
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
* * * * * * *
'''
