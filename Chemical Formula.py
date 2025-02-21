#CHEMICAL FORMULA......................
#Dee Approach............
a = list(input())
d = {}
def func(i):
    count = 1
    i += 1
    while count != 0 and i < len(a):
        if a[i] == ')':
            count -= 1
        elif a[i] == '(':
            count += 1
        i += 1
    return i

i = 0  
while i != len(a):
    if a[i] == '(':
        increment = func(i)
        j = i + 1
        while j != increment:
            if 'A' <= a[j] <= 'Z':
                if j + 1 < len(a) and 'a' <= a[j+1] <= 'z':
                    if j + 2 < len(a) and a[j+2].isdigit():
                        a[j+2] = str(int(a[j+2]) * int(a[increment]))
                    else:
                        a.insert(j+2, a[increment])
                        increment += 1
                    j += 3
                elif j + 1 < len(a) and a[j+1].isdigit():
                    a[j+1] = str(int(a[j+1]) * int(a[increment]))
                    j += 2
                else:
                    a.insert(j+1, a[increment])
                    increment += 1
                    j += 1
            elif a[j] == "(":
                s = func(j)
                a[s] = str(int(a[s]) * int(a[increment]))
                j = s + 1
            else:
                j += 1        
    i += 1
a.append("1")
a.append("1")
k = 0
while k < len(a):
    st = ""
    if 'A' <= a[k] <= 'Z':
        st += a[k]   
        if k + 1 < len(a) and 'a' <= a[k+1] <= 'z':
            st += a[k+1]     
            if k + 2 < len(a) and a[k+2].isdigit():
                if st not in d.keys():
                    d[st] = int(a[k+2])
                else:
                    d[st] += int(a[k+2])
            else:
                if st not in d.keys():
                    d[st] = 1
                else:
                    d[st] += 1
            k += 3
        elif k + 1 < len(a) and a[k+1].isdigit():
            if st not in d.keys():
                d[st] = int(a[k+1])
            else:
                d[st] += int(a[k+1])
            k += 2
        else:
            if st not in d.keys():
                d[st] = 1
            else:
                d[st] += 1
            k += 1
    else:
        k += 1

aa = list(d.keys())
aa.sort()
for i in aa:
    if d[i] > 1:
        print(i, d[i], sep="", end="")
    else:
        print(i, end="")

'''
INPUT:
Mg(OH)2
OUTPUT:
H2MgO2

INPUT:
K4(ON(SO3)2)2
OUTPUT:
K4N2O14S4
'''
