#Singly Circular Linked List.............
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class SinglyCircular:
    def __init__(self):
        self.head = None
    def Lastinsert(self,value):
        if self.head is None:
            self.head = Node(value)
            self.head.next = self.head
        else:
            temp = self.head
            new_node = Node(value)
            while temp.next is not self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    def startinsert(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node
    def posinsert(self,pos,value):
        if pos == 1:
            self.startinsert(value)
            return True
        if self.head is None:
            return False
        else:
            count,new_node = 2,Node(value)
            temp = self.head
            while count<pos and temp.next is not self.head:
                temp = temp.next
                count+=1
            if count == pos:
                new_node.next = temp.next
                temp.next = new_node
                return True
            return False
    def elementinsert(self,target,value):
        if self.head is None:
            return False
        else:
            temp = self.head
            new_node = Node(value)
            while True:
                if temp.value == target:
                    new_node.next = temp.next
                    temp.next = new_node
                    return True
                temp = temp.next
                if temp is self.head:
                    return False
    def firstdelete(self):
        if self.head is None:
            return False
        elif self.head.next is self.head:
            del self.head
            self.head = None
            return True
        else:
            temp = self.head
            while True:
                temp = temp.next
                if temp.next is self.head:
                    old = self.head
                    temp.next = old.next
                    self.head = self.head.next
                    del old
                    return True
    def lastdelete(self):
        if self.head is None:
            return False
        elif self.head.next is self.head:
            return self.firstdelete()
        else:
            temp = self.head
            while temp.next.next is not self.head:
                temp = temp.next
            deleter = temp.next
            temp.next = self.head
            del deleter
            return True
    def targetdelete(self,target):
        if self.head is None:
            return False
        elif self.head.value == target:
            if self.head.next is self.head:
                del self.head
                self.head = None
            else:
                temp = self.head
                while temp.next is not self.head:
                    temp = temp.next
                temp.next = self.head.next
                curr = self.head
                self.head = curr.next
                del curr
            return True
        else:
            temp = self.head
            while temp.next is not self.head and temp.next.value !=target:
                temp = temp.next
            if temp.next.value == target:
                tardel = temp.next
                temp.next = tardel.next
                del tardel
                return True
            return False
    def posdel(self,pos):
        if pos == 1:
            if self.head is None:
                return False
            return self.firstdelete()
        else:
            temp,count = self.head,2
            while count<pos and temp.next is not self.head:
                temp = temp.next
                count+=1
            if pos == count:
                old = temp.next
                temp.next = old.next
                del old
                return True
            return False
    def display(self):
        if self.head is None:
            print("\n\nList Is Empty..!")
        else:
            temp = self.head
            while True:
                print(temp.value,end=" ")
                temp = temp.next
                if temp is self.head:
                    return
circular = SinglyCircular()
while True:
    print("\n\n-------- Singly Circular Linked List ----------")
    print("1) Insert At Last")
    print("2) Insert At First")
    print("3) Insert By Position")
    print("4) Insert By Element")
    print("5) Delete At First")
    print("6) Delete At Last")
    print("7) Delete By Target")
    print("8) Delete By Position")
    print("9) Display")
    print("0) Exit")
    action = int(input("Enter Action To Be Taken: "))
    if action == 1:
        circular.Lastinsert(int(input("Enter Element To Be Inserted: ")))
        print("\n\nElement Inserted Successfully..!")
    elif action == 2:
        circular.startinsert(int(input("Enter Element To Be Inserted: ")))
        print("\n\nElement Inserted Successfully..!")
    elif action == 3:
        print("\n\nElement Inserted Successfully..!") if circular.posinsert(int(input("Enter Position To Be Inserted: ")),int(input("Enter Element To Be Inserted: "))) else print("\n\nPosition Not Found..!")
    elif action == 4:
        print("\n\nElement Inserted Successfully..!") if circular.elementinsert(int(input("Enter Target Element: ")),int(input("Enter Element To Be Inserted: "))) else print("\n\nTarget Not Found..!")
    elif action == 5:
        print("\n\nElement Deleted Successfully..!") if circular.firstdelete() else print("\n\nList Is Empty..!")
    elif action == 6:
        print("\n\nElement Deleted Successfully..!") if circular.lastdelete() else print("\n\nList Is Empty..!")
    elif action == 7:
        print("\n\nElement Deleted Successfully..!") if circular.targetdelete(int(input("Enter Target Element To Be Deleted: "))) else print("\n\nTarget Doesn't Exists..!")
    elif action == 8:
        print("\n\nElement Deleted Successfully..!") if circular.posdel(int(input("Enter Element Position To Be Deleted: "))) else print("\n\nInvalid Position..!")
    elif action == 9:
        print("\n\n-------- Displaying Element ---------")
        circular.display()
    elif action == 0:
        print("Exiting..!")
        exit()
    else:
        print("\n\nInvalid Action..!")
'''
-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 1
Enter Element To Be Inserted: 10


Element Inserted Successfully..!


-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying Element ---------
10

-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 2
Enter Element To Be Inserted: 5


Element Inserted Successfully..!


-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying Element ---------
5 10

-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 3
Enter Position To Be Inserted: 2
Enter Element To Be Inserted: 6


Element Inserted Successfully..!


-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying Element ---------
5 6 10

-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 4
Enter Target Element: 6
Enter Element To Be Inserted: 7


Element Inserted Successfully..!


-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying Element ---------
5 6 7 10

-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 5


Element Deleted Successfully..!


-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying Element ---------
6 7 10

-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 6


Element Deleted Successfully..!


-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying Element ---------
6 7

-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 8
Enter Element Position To Be Deleted: 2


Element Deleted Successfully..!


-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 9


-------- Displaying Element ---------
6

-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 7
Enter Target Element To Be Deleted: 6


Element Deleted Successfully..!


-------- Singly Circular Linked List ----------
1) Insert At Last
2) Insert At First
3) Insert By Position
4) Insert By Element
5) Delete At First
6) Delete At Last
7) Delete By Target
8) Delete By Position
9) Display
0) Exit
Enter Action To Be Taken: 0
Exiting..!
'''
