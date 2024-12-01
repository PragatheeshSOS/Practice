#Left Number And Right Star Triangle Pattern......
size = int(input())
for i in range(1,size+1):
    print((str(i)+str(" "))*i,str("  ")*((size-i)*2),str("* ")*i,sep="")
'''
INPUT - 3
OUTPUT
1         * 
2 2     * * 
3 3 3 * * *
INPUT - 4
OUTPUT
1             * 
2 2         * * 
3 3 3     * * * 
4 4 4 4 * * * * 
'''
