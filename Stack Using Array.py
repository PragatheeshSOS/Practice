#Stack Using Array...............
class Stack:
    def __init__(self,size):
        self.size = size
        self.array = [None]*size
        self.top = -1
    def isempty(self):
        return self.top<0
    def isfull(self):
        return self.top == self.size-1
    def push(self,value):
        if self.isfull():
            return "\n\nStack Overflow..!"
        self.top+=1
        self.array[self.top] = value
        return "\n\nSuccessfully Pushed..!"
    def peek(self):
        if self.isempty():
            return "\n\nStack Is Empty..!"
        return f"\n\nPeek: {self.array[self.top]}"
    def pop(self):
        if self.isempty():
            return "\n\nStack Underflow..!"
        self.array[self.top] = None
        self.top-=1
        return "\n\nSuccessfully Poped..!"
    def display(self):
        if self.isempty():
            print("\n\nStack Is Empty..!")
            return
        count = self.top
        print("\n\n-------- Displaying --------")
        while count>-1:
            print(self.array[count],end=" ")
            count-=1
        return
print("\n------ Stack ------")
stack = Stack(int(input("\nEnter Array Size: ")))
while True:
    print("\n\n------- Actions ------")
    print("1) IsEmpty")
    print("2) IsFull")
    print("3) Push")
    print("4) Pop")
    print("5) Peek")
    print("9) Display")
    print("0) Exit")
    action = int(input("Enter Action: "))
    if action == 1:
        print("\n\nStack Is Empty..!") if stack.isempty() else print("\n\nStack Is Not Empty..!")
    elif action == 2:
        print("\n\nStack Is Full..!") if stack.isfull() else print("\n\nStack Is Not Full..!")
    elif action == 3:
        print(stack.push(int(input("Enter Pushing Value: "))))
    elif action == 4:
        print(stack.pop())
    elif action == 5:
        print(stack.peek())
    elif action == 9:
        stack.display()
    elif action == 0:
        print("Exiting..!")
        exit()
    else:
        print("\n\nInvalid Action..!")
'''

------ Stack ------

Enter Array Size: 5


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 1


Stack Is Empty..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 2


Stack Is Not Full..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 5


Stack Is Empty..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 9


Stack Is Empty..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 4


Stack Underflow..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter Pushing Value: 10


Successfully Pushed..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter Pushing Value: 20


Successfully Pushed..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter Pushing Value: 30


Successfully Pushed..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter Pushing Value: 40


Successfully Pushed..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter Pushing Value: 50


Successfully Pushed..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------
50 40 30 20 10

------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 2


Stack Is Full..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 4


Successfully Poped..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 9


-------- Displaying --------
40 30 20 10

------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 4


Successfully Poped..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 4


Successfully Poped..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 4


Successfully Poped..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 4


Successfully Poped..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 4


Stack Underflow..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 9


Stack Is Empty..!


------- Actions ------
1) IsEmpty
2) IsFull
3) Push
4) Pop
5) Peek
9) Display
0) Exit
Enter Action: 0
Exiting..!
'''
