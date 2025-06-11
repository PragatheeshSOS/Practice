# Printing String Based On Number Inbetween...........................
string = input()
result,i = "",0
while i < len(string):
    if string[i].isalpha():
        result += string[i]
        i += 1
    elif string[i].isdigit():
        num = 0
        while i < len(string) and string[i].isdigit():
            num = num * 10 + int(string[i])
            i += 1
        if len(result) > 0:
            result = result[:-1] + result[-1] * num
print(result)
'''
| Input  | Result                   |
| ------ | ------------------------ |
| He3m2o | Heeemmo                  |
| Tryme  | Tryme                    |
| G20MA3 | GGGGGGGGGGGGGGGGGGGGMAAA |
'''
