#Max Profit Stock......
lis = [int(input()) for _ in range(int(input()))]
mini,maxi,buy,sell = 999999999,0,0,0
for i in range(len(lis)):
    if lis[i]<mini:
        mini = lis[i]
        buy = i+1
    profit = lis[i]-mini
    if profit>maxi:
        maxi = profit
        sell = i+1
print(f"Day of buying : {buy}\nDay of Selling : {sell}")
'''
INPUT:
4
250
320
190
300
OUTPUT:
Day of buying : 3
Day of Selling : 4

INPUT:
5
150
100
230
400
240
OUTPUT:
Day of buying : 2
Day of Selling : 4
'''
