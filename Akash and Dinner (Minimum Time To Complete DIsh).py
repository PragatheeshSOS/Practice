# Akash and Dinner (Minimum Time To Complete DIsh).............................
# Question............................................................
'''
Akash and Dinner
Akash got his money from CodeChef today, so he decided to have dinner outside. He went to a restaurant having N items on the menu. The i-th item on the menu belongs to the category A[i] and requires B[i] time to be cooked.
Akash wants to have a complete meal. Thus, his meal should have at least K distinct categories of food. The total time required to get all the food Akash orders is the sum of the cooking time of all the items in the order.
Help Akash find the minimum time required to have a complete meal or tell if it is not possible to do so.

Input Format
The first line will contain T, the number of test cases. Then the test cases follow.
Each test case contains three lines:
The first line of each test case contains two space-separated integers N and K, denoting the number of dishes on the menu and the number of distinct categories in a complete meal.
The second line contains N space-separated integers where the i-th integer is A[i], denoting the category of the i-th dish in the menu.
The third line contains N space-separated integers where the i-th integer is B[i], denoting the time required to cook the i-th dish in the menu.

Output Format
For each test case, output in a single line, the minimum time required to have a complete meal. If it is impossible to have a complete meal, print -1 instead.
Constraints
1<=T<=100
1<=N,K<=10^5
1<=A[i]<=10 ^9
0<=B[i]<=10 ^9
The sum of N over all test cases won't exceed 10^5

Sample Input
4
3 1
1 2 3
2 1 3
8 3
1 3 2 2 4 1 3 5
3 3 0 1 2 4 1 4
1 1
5
1
5 3
1 1 2 2 1
1 1 0 3 5
Sample Output
1
3
1
-1
Explanation
Test case 1: Akash can choose the dish with index 2 having category 2. The total time required to get the complete meal is 1.
Test case 2: Akash can choose dishes with index 3, 5, and 7 from the menu.
Dish 3: The dish has category 2 and requires time 0.
Dish 5: The dish has category 4 and requires time 2.
Dish 7: The dish has category 3 and requires time 1.
Thus, there are 3 distinct categories, and the total time to get the meal is 0 + 2 + 1 = 3. It can be shown that this is the minimum time to get the complete meal.
Test case 3: Akash can choose the only available dish having category 5. The total time required to get the complete meal is 1.
Test case 4: The total number of distinct categories available is 2, which is less than K. Thus, it is impossible to have a complete meal.
'''
from collections import defaultdict
for _ in range(int(input())):
    menu,district = map(int,input().split())
    dishes = list(map(int,input().split()))
    time = list(map(int,input().split()))
    res = defaultdict(lambda: float('inf'))
    for i in range(menu):
        currentDish = dishes[i]
        currenttime = time[i]
        if currenttime<res[currentDish]:
            res[currentDish] = currenttime
    if len(res)<district:
        print(-1)
        continue
    finalres = sorted(res.values())
    print(sum(finalres[:district]))
'''
INPUT
4
3 1
1 2 3
2 1 3
8 3
1 3 2 2 4 1 3 5
3 3 0 1 2 4 1 4
1 1
5
1
5 3
1 1 2 2 1
1 1 0 3 5
OUTPUT:
1
3
1
-1

INPUT:
1
3 1
1 2 3
2 1 3
OUTPUT:
1

INPUT:
1
8 3
1 3 2 2 4 1 3 5
3 3 0 1 2 4 1 4
OUTPUT:
3
'''
'''
EXPLANATION:
Reading Input
for _ in range(int(input())):: The code is set up to run for multiple scenarios or "test cases". It first asks how many scenarios it needs to solve.
menu, district = map(int,input().split()): In each scenario, it reads two numbers:
menu: The total number of dishes available on the menu.
district: The number of distinct dishes you need to prepare.
dishes = list(map(int,input().split())): It reads the list of dish IDs. For example, [1, 2, 1, 3].
time = list(map(int,input().split())): It reads the corresponding preparation time for each dish. For example, [10, 12, 8, 5].
Example So Far:
dishes = [1, 2, 1, 3]
time = [10, 12, 8, 5]
This means Dish 1 can be made in 10 minutes or 8 minutes. Dish 2 takes 12 minutes, and Dish 3 takes 5 minutes.
Finding the Fastest Time for Each Unique Dish
res = defaultdict(lambda: float('inf')): This creates a special dictionary to store our results. The key will be the dish ID and the value will be the minimum time found so far for that dish.
defaultdict: This is a convenient dictionary type. If you try to access a key that doesn't exist, it automatically creates it with a default value.
lambda: float('inf'): The default value is set to infinity (float('inf')). This is a clever trick for finding a minimum. Any real preparation time will be less than infinity.
The for loop then iterates through all the available dishes and their times.
if currenttime < res[currentDish]:: This is the core logic. It checks if the time for the current dish is less than the time already stored in our dictionary for that same dish.
First time seeing a dish: If we see dish 1 for the first time (with time 10), res[1] will be infinity. Since 10 < infinity, the condition is true.
Seeing a dish again: Later, we see dish 1 again, but this time with a time of 8. The code checks if 8 < res[1] (which is currently 10). This is true.res[currentDish] = currenttime: If the current time is indeed smaller, it updates the dictionary.
Example Continued: After the loop, the res dictionary would look like this: {1: 8, 2: 12, 3: 5}. It has successfully stored only the fastest time for each unique dish.
Calculating the Final Result
if len(res) < district:: It first checks if the number of unique dishes found (len(res)) is even enough to meet the requirement (district). If you need 4 distinct dishes but only 3 are available, it's impossible.
print(-1): If it's impossible, it prints -1.
finalres = sorted(res.values()): If it is possible, it takes all the minimum times from the res dictionary (e.g., [8, 12, 5]) and sorts them from smallest to largest (e.g., [5, 8, 12]).
print(sum(finalres[:district])): Finally, it takes the district fastest times from the sorted list and prints their sum. If district was 2, it would take [5, 8] and print their sum, which is 13.
'''
