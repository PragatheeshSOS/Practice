#Doubly Circular Linked List............
class Node:
    def __init__(self,value):
        self.value = value
        self.next = self.prev = None
class DoubleCircular:
    def __init__(self):
        self.head = None
    def lastinsert(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node.prev = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            new_node.next = temp.next
            temp.next.prev = new_node
            new_node.prev = temp
            temp.next = new_node
        return True
    def firstinsert(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node.prev = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = temp
            temp.next = new_node
            self.head = new_node
        return True
    def targetinsert(self,target,value):
        new_node = Node(value)
        if self.head is None:
            return False
        elif self.head.value == target:
            return self.lastinsert(value)
        else:
            temp = self.head
            while temp.value != target and temp.next is not self.head:
                temp = temp.next
            if temp.value == target:
                new_node.prev = temp
                new_node.next = temp.next
                new_node.prev.next = new_node.next.prev = new_node
                return True
            return False
    def posinsert(self,pos,value):
        if self.head is not None and pos == 1:
            return self.firstinsert(value)
        else:
            new_node,temp,count = Node(value),self.head,2
            while count<pos and temp.next is not self.head:
                temp = temp.next
                count+=1
            if pos == count:
                new_node.next = temp.next
                new_node.prev = temp
                new_node.prev.next = new_node.next.prev = new_node
                return True
        return False
    def firstdelete(self):
        if self.head is None:
            return False
        elif self.head.next is self.head:
            del self.head
            self.head = None
        else:
            old = self.head
            old.next.prev = old.prev
            old.prev.next = old.next
            self.head = old.next
            del old
        return True
    def lastdelete(self):
        if self.head is None:
            return False
        elif self.head.next is self.head:
            del self.head
            self.head = None
        else:
            last = self.head.prev
            lastbefore = last.prev
            lastbefore.next = self.head
            self.head.prev = lastbefore
            del last
        return True
    def targetdelete(self,target):
        if self.head is None:
            return False
        elif self.head.value == target:
            del self.head
            self.head = None
            return True
        else:
            temp = self.head.next
            while temp.value != target and temp.next is not self.head:
                temp = temp.next
            if temp.value == target:
                beforetarget = temp.prev
                beforetarget.next = temp.next
                temp.next.prev = beforetarget
                del temp
                return True
            return False
    def posdelete(self,pos):
        if self.head is None:
            return False
        elif pos == 1:
            return self.firstdelete()
        else:
            temp,count = self.head,2
            while count<pos and temp.next is not self.head:
                temp = temp.next
                count+=1
            if pos == count:
                target = temp.next
                target.next.prev = temp
                temp.next = target.next
                del target
                return True
            return False
    def display(self):
        if self.head == None:
            print("\n\nList Is Empty..!")
            return
        else:
            temp = self.head
            while True:
                print(temp.value,end=" ")
                temp = temp.next
                if temp is self.head:
                    print()
                    return
circular  = DoubleCircular()
while True:
    print("\n\n------ Doubly Circular Linked List ------")
    print("1) Insert At Last")
    print("2) Insert At First")
    print("3) Insert By Target")
    print("4) Insert By Position")
    print("5) Delete At First")
    print("6) Delete At Last")
    print("7) Delete By Target")
    print("8) Delete By Position")
    print("9) Display")
    print("0) Exit")
    action = int(input("Enter Action To Be Taken: "))
    if action == 1:
        print("\n\nElement Inserted Successfully..!") if circular.lastinsert(int(input("Enter Element To Be Inserted: "))) else print("\n\nError..!")
    elif action == 2:
        print("\n\nElement Inserted Successfully..!") if circular.firstinsert(int(input("Enter Element To Be Inserted: "))) else print("\n\nError..!")
    elif action == 3:
        print("\n\nElement Inserted Successfully..!") if circular.targetinsert(int(input("Enter Target Element: ")),int(input("Enter Element To Be Inserted: "))) else print("\n\nTarget Doesn't Exists..!")
    elif action == 4:
        print("\n\nElement Inserted Successfully..!") if circular.posinsert(int(input("Enter Position: ")),int(input("Enter Element To Be Inserted: "))) else print("\n\nInvalid Position..!")
    elif action == 5:
        print("\n\nElement Deleted Successfully..!") if circular.firstdelete() else print("\n\nList Is Empty..!")
    elif action == 6:
        print("\n\nElement Deleted Succesfully..!") if circular.lastdelete() else print("\n\nList Is Empty..!")
    elif action == 7:
        print("\n\nElement Deleted Successfully..!") if circular.targetdelete(int(input("Enter Target Element: "))) else print("\n\nTarget Doesn't Exists..!")
    elif action == 8:
        print("\n\nElement Deleted Successfully..!") if circular.posdelete(int(input("Enter Position: "))) else print("\n\nPosition Doesn't Exists..!")
    elif action == 9:
        print("\n\n-------- Displaying -----------")
        circular.display()
    elif action == 0:
        print("Exiting..!")
        exit()
    else:
        print("\n\nInvalid Action..!")
'''


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 1
Enter Element To Be Inserted: 10


Element Inserted Successfully..!


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying -----------
10


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 2
Enter Element To Be Inserted: 20


Element Inserted Successfully..!


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying -----------
20 10


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 3
Enter Target Element: 9
Enter Element To Be Inserted: 20


Target Doesn't Exists..!


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying -----------
20 10


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 3
Enter Target Element: 20
Enter Element To Be Inserted: 30


Element Inserted Successfully..!


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying -----------
20 10 30


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 4
Enter Position: 2
Enter Element To Be Inserted: 40


Element Inserted Successfully..!


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying -----------
20 40 10 30


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 5


Element Deleted Successfully..!


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying -----------
40 10 30


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 6


Element Deleted Succesfully..!


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying -----------
40 10


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 1
Enter Element To Be Inserted: 30


Element Inserted Successfully..!


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying -----------
40 10 30


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 8
Enter Position: 3


Element Deleted Successfully..!


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying -----------
40 10


------ Doubly Circular Linked List ------
1) Insert At Last
2) Insert At First
3) Insert By Target
4) Insert By Position
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 0
Exiting..!
'''
