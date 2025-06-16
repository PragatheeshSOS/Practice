# Apartment Allocation....................................................
# QUESTION.............................................
'''
There are n applicants and m free apartments. Your task is to distribute the apartments so that as many applicants as possible will get an apartment.
Each applicant has a desired apartment size, and they are willing to accept any apartment within a certain size range.
If the desired apartment size of an applicant is x, and the allowed difference is k, then the applicant will accept any apartment of size between x - k and x + k, inclusive.
Your goal is to match each applicant to at most one apartment, and each apartment can be assigned to at most one applicant.

INPUT
The first line contains three integers:
n – the number of applicants
m – the number of apartments
k – the maximum allowed difference in size
The second line contains n integers:
a₁, a₂, ..., aₙ – the desired apartment size for each applicant
The third line contains m integers:
b₁, b₂, ..., bₘ – the size of each available apartment

OUTPUT
Print one integer – the maximum number of applicants who can get an apartment.
1 ≤ n, m ≤ 2 × 10^5  
0 ≤ k ≤ 10^9  
1 ≤ aᵢ, bⱼ ≤ 10^9
'''
n, m, k = map(int, input().split())
wanted = sorted(list(map(int, input().split())))
available = sorted(list(map(int, input().split())))
i = j = count = 0
while i<n and j<m:
    if abs(wanted[i] - available[j]) <= k:
        count+=1
        i+=1
        j+=1
    elif wanted[i]<available[j]-k:
        i+=1
    else:
        j+=1
print(count)
'''
Input:
4 3 5
60 45 80 60
30 60 75
Output:
2

Input:
10 10 0
37 62 56 69 34 46 10 86 16 49
50 95 47 43 9 62 83 71 71 7
Output:
1

Input:
10 10 1000
59 5 65 15 42 81 58 96 50 1
18 59 71 65 97 83 80 68 92 67
Output:
10
'''
