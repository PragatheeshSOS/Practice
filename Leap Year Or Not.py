# Leap Year Or Not.......................................................................................
def isleap(year):
    return (not year%4 and year%100)>0 or (not year%100 and not year%400)>0
print("Leap Year") if isleap(int(input("Enter Year: "))) else print("Not A Leap Year")
'''
INPUT:
Enter Year: 2000
OUTPUT:
Leap Year

INPUT:
2002
OUTPUT:
Not A Leap Year

INPUT:
Enter Year: 2004
OUTPUT:
Leap Year
'''
