#Depth First Search........
nodes,edges = map(int,input("Enter Number Of Node And Number Of Edges Separated By Space: ").split())
dic,visited = {},[]
for i in range(1,nodes+1):
    dic[i] = []
for _ in range(edges):
    key,value = map(int,input("Enter Node And Its Neighbour Separated By Space: ").split())
    dic[key].append(value)
    dic[value].append(key)
stack = [int(input("Enter Starting Node: "))]
print("\n-------- DFS OUTPUT --------")
while stack:
    pop = stack.pop()
    if pop not in visited:
        print(pop,end=" ")
        visited.append(pop)
        stack.extend(reversed(dic[pop]))
'''
Enter Number Of Node And Number Of Edges Separated By Space: 6 5
Enter Node And Its Neighbour Separated By Space: 1 2
Enter Node And Its Neighbour Separated By Space: 1 3
Enter Node And Its Neighbour Separated By Space: 2 4
Enter Node And Its Neighbour Separated By Space: 2 5
Enter Node And Its Neighbour Separated By Space: 3 6
Enter Starting Node: 1

-------- DFS OUTPUT --------
1 2 4 5 3 6 
'''
