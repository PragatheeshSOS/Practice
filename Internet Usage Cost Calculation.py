# Internet Usage Cost Calculation.................................................................................................................
'''
Chef has recently got a broadband internet connection. His history of internet data usage is provided as below.
During the first T1 minutes, the internet data used was D1 MBs per minute, and during the next T2 minutes, it was D2 MBs per minute, and so on till during last TN minutes it was DN MBs per minute.
The internet provider charges the Chef 1 dollar for every 1 MB data used, except for the first K minutes, when the internet data is free as part of the plan provided to Chef.
Please find out the total amount that Chef has to pay the internet provider (in dollars).
Input
The first line of the input contains a single integer TC the number of test cases. Description of TC test cases follows.
The first line of each test case contains two space-separated integers N and K.
The next N lines of each test case contain information about the internet data usage. Specifically, in the i-th line, there will be two space-separated integers: Ti and Di.
Output
For each test case, output a single integer in a separate line, the amount that Chef has to pay in dollars.
Constraints
1 ≤ TC ≤ 1,000
1 ≤ N ≤ 10
0 ≤ K ≤ T1 + T2 + ... + TN
1 ≤ Ti, Di ≤ 10
Sample 1:
Input
3  
2 2  
2 1  
2 3  
2 2  
1 2  
2 3  
3 0  
1 2  
2 4  
10 10  
Output
6  
3  
110  
Explanation:
Example case 1: The first two minutes of internet usage are free. The last 2 minutes are charged at 3 dollars per minute, totaling 6 dollars.
Example case 2: The first two minutes are free. The last 1 minute is charged at 3 dollars per minute, totaling 3 dollars.
Example case 3: No free data usage is provided. The total cost is 1×2 + 2×4 + 10×10 = 110 dollars.
'''
for _ in range(int(input())):
    size,free = map(int,input().split())
    usage,cost = [],0
    for _ in range(size):
        time,dollor = map(int,input().split())
        usage.append([time,dollor])
    for time,dollor in usage:
        if free>=time:
            free-=time
        else:
            pay = time-free
            cost+=(pay*dollor)
            free = 0
    print(cost)
'''
INPUT:
3  
2 2  
2 1  
2 3  
2 2  
1 2  
2 3  
3 0  
1 2  
2 4  
10 10
OUTPUT:
6
3
110
'''
