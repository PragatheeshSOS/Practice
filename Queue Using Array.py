#Queue Using Array............
class Queue:
    def __init__(self,size):
        self.size = size
        self.array = [None]*size
        self.rear = -1
    def isempty(self):
        return self.rear<0
    def isfull(self):
        return self.rear == self.size-1
    def peek(self):
        if self.isempty():
            return "\n\nQueue Is Empty..!"
        return f"\n\nPeek: {self.array[0]}"
    def enqueue(self,value):
        if self.isfull():
            return "\n\nQueue Overflow..!"
        self.rear+=1
        self.array[self.rear] = value
        return "\n\nSuccessfully Enqueued..!"
    def dequeue(self):
        if self.isempty():
            return "\n\nQueue Underflow..!"
        for i in range(1,self.rear+1):
            self.array[i-1] = self.array[i]
        self.array[self.rear] = None
        self.rear-=1
        return "\n\nSuccessfully DeQueueed..!"
    def display(self):
        print("\n\n------ Displaying --------")
        if self.isempty():
            print("\n\nQueue Is Empty..!")
            return
        [print(self.array[i],end=" ") for i in range(self.rear+1)]
queue = Queue(int(input("\n\nEnter Queue Size: ")))
while True:
    print("\n\n-------- Queue --------")
    print("1) IsEmpty")
    print("2) IsFull")
    print("3) EnQueue")
    print("4) DeQueue")
    print("5) Peek")
    print("9) Display")
    print("0) Exit")
    action = int(input("Enter Action: "))
    if action == 1:
        print("\n\nQueue Is Empty..!") if queue.isempty() else print("\n\nQueue Is Not Empty..!")
    elif action == 2:
        print("\n\nQueue Is Full") if queue.isfull() else print("\n\nQueue Is Not Full")
    elif action == 3:
        print(queue.enqueue(int(input("Enter EnQueue Value: "))))
    elif action == 4:
        print(queue.dequeue())
    elif action == 5:
        print(queue.peek())
    elif action == 9:
        queue.display()
    elif action == 0:
        print("Existing..!")
        exit()
    else:
        print("\n\nInvalid Action..!")
'''


Enter Queue Size: 5


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 1


Queue Is Empty..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 2


Queue Is Not Full


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 4


Queue Underflow..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 5


Queue Is Empty..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 9


------ Displaying --------


Queue Is Empty..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter EnQueue Value: 10


Successfully Enqueued..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 5


Peek: 10


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 9


------ Displaying --------
10

-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter EnQueue Value: 20


Successfully Enqueued..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 9


------ Displaying --------
10 20

-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 4


Successfully DeQueueed..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 5


Peek: 20


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 9


------ Displaying --------
20

-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 4


Successfully DeQueueed..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 4


Queue Underflow..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter EnQueue Value: 3


Successfully Enqueued..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter EnQueue Value: 3


Successfully Enqueued..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter EnQueue Value: 3


Successfully Enqueued..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter EnQueue Value: 3


Successfully Enqueued..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter EnQueue Value: 3


Successfully Enqueued..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 3
Enter EnQueue Value: 3


Queue Overflow..!


-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 9


------ Displaying --------
3 3 3 3 3

-------- Queue --------
1) IsEmpty
2) IsFull
3) EnQueue
4) DeQueue
5) Peek
9) Display
0) Exit
Enter Action: 0
Existing..!
'''
