#Happy Number Or Not.....
number = int(input())
res = []
while number != 1 and number not in res:
    res.append(number)
    number = sum([int(i)**2 for i in str(number)])
print(str(number == 1).lower())
'''
INPUT - 19
OUTPUT - true
INPUT - 2
OUTPUT - false
INPUT - 33
OUTPUT - false
INPUT - 97
OUTPUT - true
INPUT - 1111111
OUTPUT - true
'''
