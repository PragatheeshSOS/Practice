# Removing Unbalanced Parentheses.py..........................
string = input()
paraopen,paraclose = False,False
res = ""
for i in string:
    if i not in ["(",")"]:
        res+=i
    elif i == "(" and not paraopen:
        res+=i
        paraopen = True
    elif i == ")" and paraopen and not paraclose:
        res+=i
        paraopen = False
        paraclose = False
print(res)
'''
|--------------------|-----------------|
|  INPUT             |   EXPECTED      |
|--------------------|-----------------|
| (((ab)             |    (ab)         |
|--------------------|-----------------|
| (abcd))            |    (abcd)       |
|--------------------|-----------------|
|()()((xyz)(abc)     | ()()(xyz)(abc)  |
|--------------------|-----------------|
'''
