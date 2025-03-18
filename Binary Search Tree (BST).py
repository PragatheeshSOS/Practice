#Binary Search Tree (BST)...........
'''
Deletion And Search Remains..!
'''
class Node:
    def __init__(self,value):
        self.value = value
        self.left = self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,value,traveler):
        if self.root == None:
            self.root = Node(value)
        if traveler == None:
            traveler = self.root
        elif traveler.value>value:
            if traveler.left == None:
                traveler.left = Node(value)
            else:
                self.insert(value,traveler.left)
        elif traveler.value<value:
            if traveler.right == None:
                traveler.right = Node(value)
            else:
                self.insert(value,traveler.right)
        else:
            print("Element Already Exits..!")
    def preorder(self,traveler):
        if self.root == None:
            print("Tree Is Empty..!")
        if not traveler: return
        print(traveler.value,end=" ")
        self.preorder(traveler.left)
        self.preorder(traveler.right)
    def inorder(self,traveler):
        if self.root == None:
            print("Tree Is Empty..!")
        if not traveler: return
        self.inorder(traveler.left)
        print(traveler.value,end=" ")
        self.inorder(traveler.right)
    def postorder(self,traveler):
        if self.root == None:
            print("Tree Is Empty..!")
        if not traveler: return
        self.postorder(traveler.left)
        self.postorder(traveler.right)
        print(traveler.value,end=" ")
bstree = BST()
while 1:
    print("\n\n\n--------- Binary Search Tree ---------\n1) Insertion\n2) Pre-order Traversal\n3) In-order Traveral\n4) Post-order Traversal\n0) Exit\n")
    action = int(input("Enter Number To Take Action: "))
    if action == 1:
        bstree.insert(int(input("Enter Value To Be Inserted: ")),bstree.root)
        print("\n\nElement Inserted Successfully..!")
    elif action == 2:
        print("\n\n--------- Pre-order Traveral ---------")
        bstree.preorder(bstree.root)
    elif action == 3:
        print("\n\n--------- In-order Traveral ---------")
        bstree.inorder(bstree.root)
    elif action == 4:
        print("\n\n--------- Post-order Traveral ---------")
        bstree.postorder(bstree.root)
    elif action == 0:
        print("Exiting..!")
        exit()
    else:
        print("\nEnter A Valid Input..!")
