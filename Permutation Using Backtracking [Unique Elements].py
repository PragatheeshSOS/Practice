#Permutation Using BackTracking [Unique Elements].............
# The Code Works For Input Without Repeatation.
def backtrack(lis,lis1,res):
    if len(lis1) == len(lis):
        res.append(lis1[:])
        return
    for i in lis:
        if i not in lis1:
            lis1.append(i)
            backtrack(lis,lis1,res)
            lis1.pop()
res = []
backtrack(list(input().split()),[],res)
print(res)

'''
INPUT:
a b c
OUTPUT:
[['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]

INPUT:
1 2 3
OUTPUT:
[['1', '2', '3'],
 ['1', '3', '2'],
 ['2', '1', '3'],
 ['2', '3', '1'],
 ['3', '1', '2'],
 ['3', '2', '1']]

INPUT:
a b
OUTPUT:
[['a', 'b'], ['b', 'a']]

INPUT:
x
OUTPUT:
[['x']]

INPUT:

OUTPUT:
[[]]
'''
