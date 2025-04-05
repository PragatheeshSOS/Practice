# Batsman Problem (Score Prediction)............
![1.Batsman Problem](https://github.com/user-attachments/assets/b8823ec5-f7f4-453b-9815-686fa86511e7)
string = input()
if len(string) != 6 or any(i not in "1234567890Y." for i in string):
    print("Invalid")
else:
    batsman1 = batsman2 = bowler = flag = 0
    for i in string:
        if i == "Y":
            bowler+=1
        elif i.isdigit():
            if flag == 0:
                batsman1+=int(i)
            else:
                batsman2+=int(i)
            if int(i)%2 == 1:
                flag = 1-flag
            bowler+=int(i)
    print(f"BATSMAN 1: {batsman1}\nBATSMAN 2: {batsman2}\nBOWLER: {bowler}")
'''
INPUT:
2461..
OUTPUT:
BATSMAN 1: 13
BATSMAN 2: 0
BOWLER: 13

INPUT:
......
OUTPUT:
BATSMAN 1: 0
BATSMAN 2: 0
BOWLER: 0

INPUT:
.....Y
OUTPUT:
BATSMAN 1: 0
BATSMAN 2: 0
BOWLER: 1

INPUT:
111111
OUTPUT:
BATSMAN 1: 3
BATSMAN 2: 3
BOWLER: 6

INPUT:
YYYYYY
OUTPUT:
BATSMAN 1: 0
BATSMAN 2: 0
BOWLER: 6
'''
