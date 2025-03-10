#Doubly Linked List.......
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def lastInsert(self,value):
        if self.head == None:
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        print("\nElement Inserted At Last Successfully..!")
    def startInsert(self,value):
        if self.head == None:
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value)
            self.head.prev = newNode
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
                    newNode.prev = address
                    newNode.next = address.next
                    if address.next:
                        address.next.prev = newNode
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
                if count == position-1:
                    newNode = Node(value)
                    newNode.prev = address
                    newNode.next = address.next
                    if address.next:
                        address.next.prev = newNode
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
            self.head.next.prev = None
            self.head = self.head.next
            del deleter
            print("\nFirst Element Deleted Successfully..!")
    def delLast(self):
        if self.head == None:
            print("\nList Is Already Being Empty..!")
        elif self.head.next == None:
            del self.head
            self.head = None
        else:
            deleter = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        print("\nLast Element Deleted Successfully..!")
    def delElement(self,target):
        if self.head == None:
            print("\nList Is Empty..!")
        else:
            address = self.head
            while address:
                if address.value == target:
                    if address == self.head:
                        self.head = self.head.next
                        if self.head:
                            del self.head.prev
                            self.head.prev = None
                        print("\nTarget Element Deleted Successfully..!")
                        return
                    elif address == self.tail:
                        self.tail = self.tail.prev
                        if self.tail:
                            del self.tail.next
                            self.tail.next = None
                        print("\nTarget Element Deleted Successfully..!")
                        return
                    else:
                        deleter = address
                        address.prev.next = address.next
                        address.next.prev = address.prev
                        del deleter
                        print("\nTarget Element Deleted Successfully..!")
                        return
                address = address.next
            print("\nTarget Element Not Found..!")
    def delPosition(self,position):
        if self.head == None:
            print("\nList Is Empty..!")
        else:
            address,count = self.head,0
            while address:
                if count == position-1:
                    if address == self.head:
                        self.head = self.head.next
                        if self.head:
                            del self.head.prev
                            self.head.prev = None
                        print("\nElement Deleted From Position Successfully..!")
                        return
                    elif address == self.tail:
                        self.tail = self.tail.prev
                        if self.tail:
                            del self.tail.next
                            self.tail.next = None
                        print("\nElement Deleted From Position Successfully..!")
                        return
                    else:
                        deleter = address
                        address.prev.next = address.next
                        address.next.prev = address.prev
                        del deleter
                        print("\nElement Deleted From Position Successfully..!")
                        return
                address = address.next
                count+=1
            print("\nInvalid Position. Enter Valid Position..!")
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
