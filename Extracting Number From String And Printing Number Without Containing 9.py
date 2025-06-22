# Extracting Number From String And Printing Number Without Containing 9..........................................................................................................
'''
Extract the Number from given string
Benny once had trouble finding the numbers in a string. There are various numbers in the string and you need to extract the number from the string. One catch is, you need to find only those numbers which do not contain 9. For example, if the string contains "hello this is alpha 5051 and 9475".You will extract 5051 and not 9475. Help Benny find the numbers
Input Format
The first line consists of T test cases and next T lines contain a string.
Length of each string S may be between 1 to 1000. SAMPLE INPUT: 1 Hi5 Welcome567 batch 2019
Output Format
For each string output the number stored in that string.If a string has no numbers print -1.
Constraints:
1<=T<=100
1<=|S|<=1000 SAMPLE OUTPUT: 5 567
'''
def isnum(value):
    result = ""
    for i in value:
        if i.isnumeric():
            result+=i
    return result.strip(),result.isnumeric()
for _ in range(int(input())):
    nums = []
    for i in input().split():
        ans,verify = isnum(i)
        if verify and "9" not in ans:
            nums.append(ans)
    print(*nums) if nums else print(-1)
'''
INPUT:
2
This is alpha 5057 and 97
GSLV is a satellite
OUTPUT:
5057 
-1

INPUT:
1
GSLV F11 was launched in December 19, 2018
OUTPUT:
11 2018 
'''
