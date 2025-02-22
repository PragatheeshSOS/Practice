#LINEAR SEARCH............
'''
Time Complexity = O(n)
Space Complexity = O(1)
'''
#Approach 1.............
def linear_search(lis,target):
    for i in range(len(lis)):
        if lis[i] == target:
            return f"{target} Found At Index {i}."
    return f"{target} Not Found."

lis,target = input("Enter Elements Separated By Space: ").split(),input("Enter Target Value: ")
print(linear_search(lis,target))

# Approach 2.............
lis,target = input("Enter Elements Separated By Space: ").split(),input("Enter Target Value: ")
print(f"{target} Found At Index {lis.index(target)}.") if target in lis else print(f"{target} Not Found.")

'''
INPUT:
Enter Elements Separated By Space: 12 34 56 78 34
Enter Target Value: 56
OUTPUT:
56 Found At Index 2.

INPUT:
Enter Elements Separated By Space: 34 546  758 79
Enter Target Value: 12
OUTPUT:
12 Not Found.
'''
