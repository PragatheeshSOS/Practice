# Longest Consecutive Sequence Length.......................................................................................
# QUESTION...............................
'''
Write a  program to find the length of the longest consecutive elements sequence from a given unsorted array of integers. The sequence is identified assuming the array is sorted before evaluating.
If two sequences have same longest length return 0.

Sample array 1:
49, 1, 3, 200, 2, 4, 70, 5
The longest consecutive elements sequence is 1, 2, 3, 4, 5 therefore the program will return its length 5.
Output
5

Sample array 2:
56, 4 ,3 ,8, 7, 9
The longest consecutive elements sequence is 7,8,9 therefore the program will return its length 3.
Output
3

For example:
Input	Result
49 1 3 200 2 4 70 5
5
56 4 3 8 7 9
3
1 2 3 4 9 8 7 6 
0
'''
lis = sorted(list(map(int, input().split())))
res,count = [],1
for i in range(1,len(lis)):
    if lis[i] == lis[i-1]+1:
        count+=1
    else:
        if count>1:
            res.append(count)
        count = 1
if count > 1:
    res.append(count)
print(max(res)) if len(set(res)) == len(res) else print(0)
'''
INPUT:
49 1 3 200 2 4 70 5
OUTPUT:
5

INPUT:
56 4 3 8 7 9
OUTPUT:
3

INPUT:
1 2 3 4 9 8 7 6
OUTPUT:
0
'''
