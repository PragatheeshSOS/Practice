# Balanced Question Checker..................
# Question......................................
'''
Naveen wants to organize a contest. Predicting difficulty levels of the problems can be a daunting task. Naveen wants his contests to be balanced in terms of difficulty levels of the problems.
Assume a contest had total P participants. A problem that was solved by at least half of the participants (i.e. P / 2 (integer division)) is said to be cakewalk difficulty. A problem solved by at max P / 10 (integer division) participants is categorized to be a hard difficulty.
Naveen wants the contest to be balanced. According to him, a balanced contest must have exactly 1 cakewalk and exactly 2 hard problems. You are given the description of N problems and the number of participants solving those problems. Can you tell whether the contest was balanced or not?

Input
The first line of the input contains an integer T denoting the number of test cases.
The first line of each test case contains two space separated integers, N, P denoting the number of problems, number of participants respectively.
The second line contains N space separated integers, i-th of which denotes number of participants solving the i-th problem.

Output
For each test case, output "yes" or "no" (without quotes) denoting whether the contest is balanced or not.

Constraints
1 ≤ T, N ≤ 500
1 ≤ P ≤ 10⁸
1 ≤ Number of participants solving a problem ≤ P

Subtasks
Subtask #1 (40 points): P is a multiple of 10
Subtask #2 (60 points): Original constraints
'''
for _ in range(int(input())):
    size,member = map(int,input().split())
    lis = list(map(int,input().split()))
    cakecount,hardcount = 0,0
    cake,hard = member//2,member//10
    for i in lis:
        if i>=cake:
            cakecount+=1
        elif i<=hard:
            hardcount+=1
    print("yes") if cakecount == 1 and hardcount == 2 else print("no")
'''
INPUT:
6             # Testcase
3 100         # size, memeber
10 1 100      # members
3 100         # size, memeber
11 1 100      # memeber
3 100         # size, memeber
10 1 10       # memeber
3 100         # size, memeber
10 1 50       # memeber
4 100         # size, memeber
50 50 50 50   # memeber
4 100         # size, memeber
1 1 1 1       # memeber
OUTPUT:
yes
no
no
yes
no
no

INPUT:
1
4 50
5 4 3 2
OUTPUT:
no

INPUT:
1
6 200
100 5 4 3 2 1
OUTPUT:
no
'''
