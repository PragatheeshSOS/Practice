# Reversed Of Letter And Hex Of Count Of Letter.......................................................................
'''
You are given a string S. Every sub-string of identical letters is replaced by a single instance of that letter followed by the hexadecimal representation of the number of occurrences of that letter. Then, the string thus obtained is further encrypted by reversing it [ See the sample for more clarity ]. Print the Encrypted String.
Note: All Hexadecimal letters should be converted to Lowercase letters.
Input:
S = "aaaaaaaaaaa"
Output:
ba 
Explanation: 
aaaaaaaaaaa
Step1: a11 (a occurs 11 times)
Step2: a11 is ab [since 11 is b in
hexadecimal]
Step3: ba [After reversing]
For example:
Input	Result
aaaaaaaaaaa
ba
'''
string = input()
stack = []
res = ""
for i in string:
    if i not in stack:
        count = hex(string.count(i))[2:]
        res+=(i+count)
        stack.append(i)
print(*res[::-1],sep="")
'''
| Input       | Output |
| ----------- | ------ |
| aaaaaaaaaaa | ba     |
| aabbccc     | 3c2b2a |
| zzzzzzzzzz  | az     |
'''
