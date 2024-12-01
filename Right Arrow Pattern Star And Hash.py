#Right Arrow Pattern Star And Hash......
size = int(input())
for i in range(1,size+1):
    print(str("* ")*i) if i%2 != 0 else print(str("# ")*i)
for i in range(size,-1,-1):
    print(str("* ")*(i)) if i%2 == 0 else print(str("# ")*(i))
'''
INPUT - 3
OUTPUT
*
# #
* * *
# # #
* *
#
INPUT - 7
OUTPUT
* 
# # 
* * * 
# # # # 
* * * * * 
# # # # # # 
* * * * * * * 
# # # # # # # 
* * * * * * 
# # # # # 
* * * * 
# # # 
* * 
# 
'''
