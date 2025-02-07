#Bubble Sort..........

'''
Average And Worst Time Complexity = O(n**2)
Best Time Complexity = O(n)
Space Complexity (Best,Average,Worst) = O(1)
Total Number Of Comparsion = n(n-1)/2
'''

def bubblesort(lis):
    print()
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
