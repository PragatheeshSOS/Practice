#Printing ASC And DESC Number Alternatively......
lis = [i for i in range(1,int(input())+1)]
lisrev = lis[::-1]
for i in range(len(lis)):
    print(lis[i],lisrev[i],end=" ")
'''
INPUT - 7
OUTPUT - 1 7 2 6 3 5 4 4 5 3 6 2 7 1
INPUT - 5
OUTPUT - 1 5 2 4 3 3 4 2 5 1
'''
