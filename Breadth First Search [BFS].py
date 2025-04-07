#Breadth First Search........
nodes,edges = map(int,input("Enter Number Of Node And Number Of Edges Separated By Space: ").split())
dic,visited = {},[]
for i in range(1,nodes+1):
    dic[i] = []
for _ in range(edges):
    key,value = map(int,input("Enter Node And Its Neighbour Separated By Space: ").split())
    dic[key].append(value)
    dic[value].append(key)
queue = [int(input("Enter Starting Node: "))]
print("\n-------- BFS OUTPUT --------")
while queue:
    pop = queue.pop(0)
    if pop not in visited:
        print(pop,end=" ")
        visited.append(pop)
        queue.extend(dic[pop])
'''
Enter Number Of Node And Number Of Edges Separated By Space: 6 5
Enter Node And Its Neighbour Separated By Space: 1 2
Enter Node And Its Neighbour Separated By Space: 1 3
Enter Node And Its Neighbour Separated By Space: 2 4 
Enter Node And Its Neighbour Separated By Space: 2 5
Enter Node And Its Neighbour Separated By Space: 3 6
Enter Starting Node: 1

-------- BFS OUTPUT --------
1 2 3 4 5 6 
'''
