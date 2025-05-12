# Sum Game (Gradle's Crazy Game)............
#QUESTION...............
# Gradle and Bob take turns playing a game, with Gradle starting first.
# You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:
# Choose an index i where num[i] == '?'.
# Replace num[i] with any digit between '0' and '9'.
# The game ends when there are no more '?' characters in num.
# For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Gradle to win, the sums must not be equal.
# For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Gradle wins because 2+4+3 != 8+0+3.
# Assuming Gradle and Bob play optimally, return true if Gradle will win and false if Bob will win.
game = input()
gradle,bob = 0,0
questiongrad,questionbob = 0,0
half = len(game)//2
for i in range(half):
    if game[i].isdigit():
        gradle+=int(game[i])
    else:
        questiongrad+=1
for i in range(half,len(game)):
    if game[i].isdigit():
        bob+=int(game[i])
    else:
        questionbob+=1
subract = gradle - bob
question = questionbob - questiongrad
print("true") if subract != 9*((question)//2) else print("false")  #Reference Link - https://www.perplexity.ai/search/original-input-count-question-xCDTJulBR.CbR5PL4IKtkw
# Why this formula? [subtract != 9*((question)//2] 
# Each player can choose the value for a '?' on their turn.
# The maximum difference a player can force is by always picking 9 for their half and 0 for the other half.
# The difference in the number of '?' between halves (questionbob - questiongrad) determines who has more power to influence the sum.
# Dividing by 2 (// 2) is because players alternate picks.
# Multiplying by 9 is because the maximum digit is 9.
# If the current difference in sums (subtract) can be balanced out by the difference in question marks, Bob can force a tie; otherwise, Gradle can force a win.
'''
INPUT:
243801
OUTPUT:
false

INPUT:
25??
OUTPUT:
true
'''
