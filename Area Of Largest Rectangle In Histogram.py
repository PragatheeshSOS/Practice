#AREA OF LARGEST RECTANGLE IN HISTOGRAM......(All Pass Only On Portal)

def forward(current):
    now = given[current]
    location = current
    for i in range(current,len(given)):
        if now<=given[i]:
            location = i
        else:
            break
    return location
    
def backward(current):
    now = given[current]
    location = current
    for i in range(current,-1,-1):
        if now<=given[i]:
            location = i
        else:
            break
    return location

given,final = eval(input()),[]
for i in range(len(given)):
    final.append(((forward(i)-backward(i))+1)*given[i])
print(max(final))

'''
INPUT:
[2,1,5,6,2,3]
OUTPUT:
10

INPUT:
[2,4]
OUTPUT:
4


'''
