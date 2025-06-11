# Max Stock Profit With Day Of Buy,Sell And Profit....................................................
lis = [int(input()) for _ in range(int(input()))]
min_price,buy_day,max_profit,best_buy_day,best_sell_day = lis[0],1,0,1,1
for i in range(1, len(lis)):
    if lis[i] - min_price > max_profit:
        max_profit = lis[i] - min_price
        best_buy_day = buy_day
        best_sell_day = i + 1
    if lis[i] < min_price:
        min_price = lis[i]
        buy_day = i + 1
print(f"Day of buying : {best_buy_day}")
print(f"Day of Selling : {best_sell_day}")
print(f"Profit: {max_profit}")
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
Profit: 110

INPUT:
5  
150  
100  
230  
400  
50
OUTPUT:
Day of buying : 2  
Day of Selling : 4  
Profit: 300

INPUT:
4  
100  
50  
90  
5
OUTPUT:
Day of buying : 2  
Day of Selling : 3  
Profit: 40
'''
