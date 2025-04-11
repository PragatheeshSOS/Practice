#Stack Using Linked List..........
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def isempty(self):
        return self.head == None
    def push(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        return "\n\nSuccessfully Pushed..!"
    def peek(self):
        if self.isempty():
            return "\n\nStack Is Empty..!"
        return f"\n\nPeek: {self.head.value}"
    def pop(self):
        if self.isempty():
            return "\n\nStack Is Empty..!"
        oldhead = self.head
        self.head = self.head.next
        del oldhead
        return "\n\nSuccessfully Poped..!"
    def display(self):
        print("\n\n-------- Displaying --------")
        if self.isempty():
            print("\n\nStack Is Empty..!")
            return
        temp = self.head
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next
stack = Stack()
while True:
    print("\n\n------- Stack --------")
    print("1) IsEmpty")
    print("2) Push")
    print("3) Pop")
    print("4) Peek")
    print("9) Display")
    print("0) Exit")
    action = int(input("Enter Action: "))
    if action == 1:
        print("\n\nStack Is Empty..!") if stack.isempty() else print("\n\nStack Is Not Empty..!")
    elif action == 2:
        print(stack.push(int(input("Enter Pushing Value: "))))
    elif action == 3:
        print(stack.pop())
    elif action == 4:
        print(stack.peek())
    elif action == 9:
        stack.display()
    elif action == 0:
        print("Exiting..!")
        exit()
    else:
        print("\n\nInvalid Action..!")
'''


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 1


Stack Is Empty..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 3


Stack Is Empty..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------


Stack Is Empty..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 4


Stack Is Empty..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 2
Enter Pushing Value: 10


Successfully Pushed..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 4


Peek: 10


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------
10

------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 3


Successfully Poped..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------


Stack Is Empty..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 2
Enter Pushing Value: 20


Successfully Pushed..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------
20

------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 2
Enter Pushing Value: 30


Successfully Pushed..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 1


Stack Is Not Empty..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 4


Peek: 30


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------
30 20

------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 3


Successfully Poped..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------
20

------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 3


Successfully Poped..!


------- Stack --------
1) IsEmpty
2) Push
3) Pop
4) Peek
9) Display
0) Exit
Enter Action: 0
Exiting..!
'''
