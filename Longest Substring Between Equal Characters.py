# Longest Substring Between Equal Characters..................................................................................................
'''
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
A substring is a contiguous sequence of characters within a string.
Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
Constraints:
1 <= s.length <= 300
s contains only lowercase English letters.
For example:
Input	Result
bb
0
akarsvkp
4
'''
string = input()
if len(string) == len(set(string)):
    print(-1)
else:
    res = -1
    for i in string:
        if string.count(i)>1:
            left,right = string.index(i),string.rindex(i)
            res = max(res,right-left-1)
    print(res)
'''
INPUT:
bb
OUTPUT:
0
INPUT:
akarsvkp
OUTPUT:
4
'''
