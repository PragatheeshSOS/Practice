#Printing Array Element Using Recursion(Printing List Element By Recursive Method)...........
def arrprint(lis,size,i):
    if size == i:
        return
    print(lis[i],end=" ")
    i+=1
    arrprint(lis,size,i)
size,lis = int(input("Enter Size Of Array: ")),list(map(int,input("Enter Elements Separated By Space: ").split()))
arrprint(lis,size,0)
'''
INPUT:
4
1 2 4 4
OUTPUT:
1 2 4 4
'''
