# Is Perfect Square And Cube...............................................................................................................................
def isperfect(number):
    return (round(number ** 0.5) ** 2 == number) or (round(number ** (1/3)) ** 3 == number)
print(isperfect(int(input("Enter Number: "))))
'''
INPUT:
Enter Number: 5
OUTPUT:
False

INPUT:
Enter Number: 64
OUTPUT:
True

INPUT:
Enter Number: 729
OUTPUT:
True
'''
