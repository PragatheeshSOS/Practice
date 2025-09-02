'''
QUESTION:
College Life 4
Read problem statements in Bengali, Mandarin Chinese, Russian, and Vietnamese as well.
Arjun and N-1 more of his friends go to the night canteen. The canteen serves only three items (well, they serve more, but only these three are edible!), which are omelette, chocolate milkshake, and chocolate cake. Their prices are A, B and C, respectively.
However, the canteen is about to run out of some ingredients. In particular, they only have E eggs and H chocolate bars left. They need:
2 eggs to make an omelette.
3 chocolate bars for a chocolate milkshake.
1 egg and 1 chocolate bar for a chocolate cake.
Each of the N friends wants to order one item. They can only place an order if the canteen has enough ingredients to prepare all the ordered items. Find the smallest possible total price they have to pay or determine that it is impossible to prepare N items.
Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains six space-separated integers N, E, H, A, B and C.
Output
For each test case, print a single line containing one integer — the minimum cost of N items, or -1 if it is impossible to prepare N items.
'''
# College Life 4 (Maximum Food In Lowest Cast)...............................................
for _ in range(int(input())):
    N,E,H,A,B,C = map(int,input().split())
    ans = float('inf')
    for cakes in range(0,min(E,H,N)+1):
        remaining = N-cakes
        eggs_left = E-cakes
        choc_left = H-cakes
        cost = cakes*C
        if A<B:
            omelettes = min(eggs_left//2,remaining)
            milkshakes = remaining-omelettes
        else:
            milkshakes = min(choc_left//3,remaining)
            omelettes = remaining-milkshakes
        if omelettes>=0 and milkshakes>=0 and omelettes*2<=eggs_left and milkshakes*3<=choc_left:
            total_cost = cost+omelettes*A+milkshakes*B
            ans = min(ans,total_cost)
    print(-1 if ans == float('inf') else ans)
'''
Input	          Result
3	
5 4 4 2 2 2	     -1
4 5 5 1 2 3	      7
4 5 5 3 2 1	      4

1	
1 0 0 1 1 1    	 -1

1
4 4 4 10 20 1     4
'''
