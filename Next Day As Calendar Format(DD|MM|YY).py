# Next Day As Calendar Format(DD|MM|YY)...............................................................................................................
# APPROACH 1......................................................................................................
def isleap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
day, month, year = map(int, input().split("/"))
if month == 2:
    if isleap(year):
        if day<29:
            print(f"{day+1:02}/{month:02}/{year}")
        else:
            print(f"01/{month+1:02}/{year}")
    else:
        if day<28:
            print(f"{day+1:02}/{month:02}/{year}")
        else:
            print(f"01/{month+1:02}/{year}")
elif month in [4, 6, 9, 11]:
    print(f"{day+1:02}/{month:02}/{year}") if day < 30 else print(f"01/{month+1:02}/{year}")
elif month in [1, 3, 5, 7, 8, 10, 12]:
    if day<31:
        print(f"{day+1:02}/{month:02}/{year}")
    else:
        if month == 12:
            print(f"01/01/{year+1:02}")
        else:
            print(f"01/{month+1:02}/{year}")
          
# APPROACH 2......................................................................................................
def isleap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def max_day(month, year):
    if month == 2:
        return 29 if isleap(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
day, month, year = map(int, input().split("/"))
if day < max_day(month, year):
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print(f"{day:02}/{month:02}/{year}")
'''
INPUT:
28/02/2024
OUTPUT:
29/02/2024

INPUT:
31/12/2025
OUTPUT:
01/01/2026

INPUT:
31/01/2022
OUTPUT:
01/02/2022

INPUT:
28/01/2020
OUTPUT:
29/01/2020
'''
