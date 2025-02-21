#AREA OF LARGEST RECTANGLE IN HISTOGRAM......
#PortPass Approach.............
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

#Mug Approach...............
hist = eval(input())
max_size = 0
stack = []
for i in range(len(hist)):
    if stack == [] or stack[-1][0] <= hist[i]:
        stack.append((hist[i], i))
    else:
        while stack and stack[-1][0] >= hist[i]:
            num = stack.pop()
            max_size = max(max_size, num[0]*(i-num[1]))
        stack.append((hist[i], num[1]))

while stack:
    num = stack.pop()
    max_size = max(max_size, num[0]*(len(hist)-num[1]))

print(max_size)

#Dee Approach................
a=eval(input())
b=[]
for i in range(len(a)):
    step=1
    maxi=a[i]
    for j in range(i+1,len(a)):
        if a[j]>=a[i]:
            if a[j]>=maxi:
                maxi=a[j]
            step+=1
        else:
            break
    c=step*a[i]
    if maxi>=c:
        b.append(maxi)
    else:
        b.append(c)
for i in range(len(a)-1,-1,-1):
    step=1
    maxi=a[i]
    for j in range(i-1,-1,-1):
        if a[j]>=a[i]:
            if a[j]>=maxi:
                maxi=a[j]
            step+=1
        else:
            break
    c=step*a[i]
    if maxi>=c:
        b.append(maxi)
    else:
        b.append(c)
print(max(b))
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
