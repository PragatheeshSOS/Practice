#Queue Using Linked List............
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.rear = self.front = None
    def isempty(self):
        return self.front is None
    def enqueue(self,value):
        new_node = Node(value)
        if self.isempty():
            self.rear = self.front = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        return "\n\nSuccessfully EnQueued..!"
    def peek(self):
        if self.isempty():
            return "\n\nQueue Is Empty..!"
        return f"\n\nPeek: {self.front.value}"
    def dequeue(self):
        if self.isempty():
            return "\n\nQueue Underflow..!"
        oldfront = self.front
        self.front = oldfront.next
        del oldfront
        return "\n\nSuccessfully DeQueued..!"
    def display(self):
        print("\n\n-------- Displaying --------")
        if self.isempty():
            print("\n\nQueue Is Empty..!")
            return
        temp = self.front
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next
queue = Queue()
while True:
    print("\n\n------ Queue ------")
    print("1) IsEmpty")
    print("2) EnQueue")
    print("3) DeQueue")
    print("4) Peek")
    print("9) Display")
    print("0) Exit")
    action = int(input("Enter Action: "))
    if action == 1:
        print("\n\nQueue Is Empty..!") if queue.isempty() else print("\n\nQueue Is Not Empty..!")
    elif action == 2:
        print(queue.enqueue(int(input("Enter EnQueue Value: "))))
    elif action == 3:
        print(queue.dequeue())
    elif action == 4:
        print(queue.peek())
    elif action == 9:
        queue.display()
    elif action == 0:
        print("Exiting..!")
        exit()
    else:
        print("\n\nInvalid Action..!")
'''


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 1


Queue Is Empty..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 3


Queue Underflow..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------


Queue Is Empty..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 4


Queue Is Empty..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 2
Enter EnQueue Value: 10


Successfully EnQueued..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 1


Queue Is Not Empty..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 4


Peek: 10


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------
10

------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 2
Enter EnQueue Value: 20


Successfully EnQueued..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------
10 20

------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 4


Peek: 10


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 3


Successfully DeQueued..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------
20

------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 4


Peek: 20


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 1


Queue Is Not Empty..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 3


Successfully DeQueued..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------


Queue Is Empty..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 4


Queue Is Empty..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 1 


Queue Is Empty..!


------ Queue ------
1) IsEmpty
2) EnQueue
3) DeQueue
4) Peek
9) Display
0) Exit
Enter Action: 0
Exiting..!
'''
