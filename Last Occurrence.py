#Last Occurrence......................
# Approach 1 (Using Recursion)..............
def lastOcc(lis,size,target):
    if size == 0:
        print("Element Not Found.")
        return
    if lis[size] == target:
        print("Element Found At Index:",size)
        return
    lastOcc(lis,size-1,target)
size,lis = int(input("Enter Size: "))-1,list(map(int,input("Enter Elements Separated By Space: ").split()))
target = int(input("Enter Target Element: "))
lastOcc(lis,size,target)

#Approach 2 (For Loop)................
lis,target = list(map(int,input("Enter Value Separated By Space: ").split())),int(input("Enter Target Element: "))
for i in range(len(lis)-1,-1,-1):
    if lis[i] == target:
        print("Element Found At Index:",i)
        exit(0)
print("Element Not Found.")

#Approach 3 (While Loop).............
size,lis,target = int(input("Enter Size: "))-1,list(map(int,input("Enter Values Of Element: ").split())),int(input("Enter Targer Value: "))
while size>0:
    if lis[size] == target:
        print("Element Found At Index:",size)
        exit()
    size-=1
print("Element Not Found.")
'''
INPUT:
Enter Size: 4
Enter Elements Separated By Space: 1 2 4 3
Enter Target Element: 4
OUTPUT:    
Element Found At Index: 2

INPUT:
Enter Size: 6
Enter Elements Separated By Space: 2 4 3 5 6 7
Enter Target Element: 1
OUTPUT:     
Element Not Found.
'''
