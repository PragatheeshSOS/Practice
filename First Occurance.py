#First Occurance......................
# Approach 1 (Using Recursion)..............
def firstOcc(lis,size,target,index):
    if size == index:
        print("Element Not Found.")
        return
    if lis[index] == target:
        print("Element Found At Index:",index)
        return
    firstOcc(lis,size,target,index+1)
size,lis = int(input("Enter Size: ")),list(map(int,input("Enter Elements Separated By Space: ").split()))
target = int(input("Enter Target Element: "))
firstOcc(lis,size,target,0)

#Approach 2 (For Loop)................
lis,target = list(map(int,input("Enter Value Separated By Space: ").split())),int(input("Enter Target Element: "))
for i in range(len(lis)):
    if lis[i] == target:
        print("Element Found At Index:",i)
        exit(0)
print("Element Not Found.")

#Approach 3 (While Loop).............
size,lis,target,i = int(input("Enter Size: ")),list(map(int,input("Enter Values Of Element: ").split())),int(input("Enter Targer Value: ")),0
while i<size:
    if lis[i] == target:
        print("Element Found At Index:",i)
        exit()
    i+=1
print("Element Not Found.")
"""
INPUT:
Enter Size: 6
Enter Elements Separated By Space: 1 2 3 4 6 9
Enter Target Element: 5
OUTPUT:
Element Not Found.

INPUT:
Enter Size: 5
Enter Elements Separated By Space: 5 4 6 3 1
Enter Target Element: 3
OUTPUT:
Element Found At Index:  3
"""
