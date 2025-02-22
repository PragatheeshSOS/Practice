#Bubble Sort..........
#Efficient Approach.........
'''
Time Complexity = O(n**2)
Space Complexity = O(1)
'''
def bubblesort(lis):
    for i in range(len(lis)):
        swap = False
        for j in range(len(lis)-i-1):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
                swap = True
        if not swap:
            return lis
        print(*lis,end=" -> ")
        print(lis[j],lis[j+1])
    return lis
print("\nFinal Result: ",*bubblesort(list(map(int,input("Enter Input: ").split()))))
'''
Enter Input: 2 3 4 3 4 2 4 5
2 3 3 4 2 4 4 5 -> 4 5
2 3 3 2 4 4 4 5 -> 4 4
2 3 2 3 4 4 4 5 -> 4 4
2 2 3 3 4 4 4 5 -> 3 4

Final Result:  2 2 3 3 4 4 4 5
# ---------------------------------
Enter Input: 10 20 30 40 50

### SWAP BREAK THE LOOP(O(n**2) -> O(n)) If Sorted. Making Its As Best Case. ###
Final Result:  10 20 30 40 50
'''

#Inefficient Approach.........
def bubblesort(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
        print(*lis)

bubblesort(list(map(int,input().split())))
'''
INPUT:
32 3 23 5 56 67 2
OUTPUT:
3 23 5 32 56 2 67
3 5 23 32 2 56 67
3 5 23 2 32 56 67
3 5 2 23 32 56 67
3 2 5 23 32 56 67
2 3 5 23 32 56 67

INPUT:
23 3 4 5 6 7
OUTPUT:
3 4 5 6 7 23
3 4 5 6 7 23
3 4 5 6 7 23
3 4 5 6 7 23
3 4 5 6 7 23
'''
