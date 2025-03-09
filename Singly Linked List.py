#Singly Linked List.......
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def lastInsert(self,value):
        if self.head == None:
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        print("\nElement Inserted At Last Successfully..!")
    def startInsert(self,value):
        if self.head == None:
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
        print("\nElement Inserted At Beginning Successfully..!")
    def elementInsert(self,value,Target):
        if self.head == None:
            print("\nList Is Empty..!")
        else:
            address = self.head
            while address:
                if address.value == Target:
                    newNode = Node(value)
                    newNode.next = address.next
                    address.next = newNode
                    print("\nElement Inserted After The Target Element Successfully..!")
                    return
                address = address.next
            print("\nTarget Element Not Found..!")
    def positionInsert(self,value,position):
        if self.head == None:
            print("\nList Is Empty..!")
        else:
            address,count = self.head,0
            while address:
                if count == position:
                    newNode = Node(value)
                    newNode.next = address.next
                    address.next = newNode
                    print("\nElement Inserted At Position Successfully..!")
                    return
                count+=1
            print("\nInvalid Position. Enter A Valid Position..!")
    def delFirst(self):
        if self.head == None:
            print("\nList Is Already Being Empty..!")
        else:
            deleter = self.head
            self.head = self.head.next
            del deleter
            print("\nFirst Element Deleted Successfully..!")
    def delLast(self):
        if self.head == None:
            print("\nList Is Already Being Empty..!")
            return
        elif self.head.next == None:
            del self.head
            self.head = None
        else:
            address = self.head
            while address.next.next:
                address = address.next
            deleter = address.next
            address.next = None
            del deleter
        print("\nLast Element Deleted Successfully..!")
    def delElement(self,target):
        if self.head == None:
            print("\nList Is Empty..!")
        else:
            address = self.head
            if self.head.value == target:
                deleter = self.head
                self.head = deleter.next
                del deleter
                print("\nTarget Element Deleted Successfully..!")
                return
            while address:
                if address.next.value == target:
                    deleter = address.next
                    address.next = deleter.next
                    del deleter
                    print("\nTarget Element Deleted Successfully..!")
                    return
                address = address.next
            print("\nTarget Element Not Found..!")
    def delPosition(self,position):
        if self.head == None:
            print("\nList Is Empty..!")
        else:
            if position == 1:
                deleter = self.head
                self.head = deleter.next
                del deleter
                print("\nElement Deleted From The Position Successfully..!")
                return
            address,count = self.head,1
            while address.next != None:
                if count == position-1:
                    deleter = address.next
                    address.next = deleter.next
                    del deleter
                    print("\nElement Deleted From The Position Successfully..!")
                    return
                address = address.next
                count+=1
            print("\n Invalid Positon. Enter A Valid Position..!")
    def display(self):
        if self.head == None:
            print("\nList Is Empty..!")
        else:
            print("\n-------- Displaying The Elements --------")
            address = self.head
            while address:
                print(address.value,end=" ")
                address = address.next
            print("\n------------------------")
Singly = LinkedList()
while(1):
    action = int(input("\n\n-------- Numbers To Action --------\n\n1) Insert At Beginning\n2) Insert At Last\n3) Insert After Element\n4) Insert At Position\n5) Delete At First\n6) Delete At Last\n7) Delete By Element\n8) Delete By Position\n9) Display\n0) Exit\n\nEnter Number To Action: "))
    if action == 1:
        Singly.startInsert(int(input("Enter The Element To Be Inserted At Beginning: ")))
    elif action == 2:
        Singly.lastInsert(int(input("Enter The Element To Be Inserted At Last: ")))
    elif action == 3:
        Singly.elementInsert(int(input("Enter The Element To Be Inserted: ")),int(input("Enter Target Element: ")))
    elif action == 4:
        Singly.positionInsert(int(input("Enter The Element To Be Inserted: ")),int(input("Enter Inserting Position: ")))
    elif action == 5:
        Singly.delFirst()
    elif action == 6:
        Singly.delLast()
    elif action == 7:
        Singly.delElement(int(input("Enter Deleting Element: ")))
    elif action == 8:
        Singly.delPosition(int(input("Enter Deleting Position: ")))
    elif action == 9:
        Singly.display()
    elif action == 0:
        exit()
