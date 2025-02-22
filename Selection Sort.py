#SELECTION SORT...............
def selectionsort(lis):
    for i in range(len(lis)-1):
        mini = i
        for j in range(i+1,len(lis)):
            if lis[mini]>lis[j]:
                mini = j
        lis[i],lis[mini] = lis[mini],lis[i]
        print(f"{i+1} ->",*lis)
    return lis
print("Sorted List: ",*selectionsort(list(map(int,input("Enter Elements Separated By Space: ").split()))))
'''
Enter Elements Separated By Space: 34 12 32 43 78 9 64
1 -> 9 12 32 43 78 34 64
2 -> 9 12 32 43 78 34 64
3 -> 9 12 32 43 78 34 64
4 -> 9 12 32 34 78 43 64
5 -> 9 12 32 34 43 78 64
6 -> 9 12 32 34 43 64 78
Sorted List:  9 12 32 34 43 64 78

Enter Elements Separated By Space: 12 34 54 45
1 -> 12 34 54 45
2 -> 12 34 54 45
3 -> 12 34 45 54
Sorted List:  12 34 45 54
'''
