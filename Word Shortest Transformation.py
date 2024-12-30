start,end,*lis = input().split()
if end not in lis:
    print("null")
else:
    start,end,res = list(start),list(end),[start]
    for i in range(len(end)):
        start[len(end)-1-i] = end[len(end)-1-i]
        strings = ""
        for j in start:
            strings+=j
        res.append(strings)
    print(*res)
    
'''
INPUT:
dog cat dot dop dat cat
OUTPUT:
dog dot dat cat

INPUT:
dog cat dot tod dat dar
OUTPUT:
null
'''
