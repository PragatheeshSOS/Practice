# Minimum Deletion To Get Equal String.......................................................
'''
You have been given two strings s1 and s2.Using the following rule,return the least number of steps required to make s1 equals to s2.
Rule:
Delete one character at a time in a string
Example:
Input:
s1="rolex"
s2="alex"
Output:
3
step 1: delete 'r' from s1 => "olex"
step 2: delete 'o' from s1 => "lex"
step 3: delete 'a' from s2 => "lex"
So the total number of steps required is 3.
'''
string1,string2 = input(),input()
lis = [[0]*(len(string2)+1) for _ in range(len(string1)+1)]
for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i] == string2[j]:
            lis[i+1][j+1] = lis[i][j]+1
        else:
            lis[i+1][j+1] = max(lis[i+1][j],lis[i][j+1])
print((len(string1)-lis[-1][-1])+(len(string2)-lis[-1][-1]))
'''
INPUT:
rolex
alex
OUTPUT:
3

INPUT:
abcdef
azced
OUTPUT:
5
'''
