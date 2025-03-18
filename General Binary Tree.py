#Binary Tree................
'''
In General Binary Tree, We Can Coding Where The Element To Be Inserted Weather Left/Right. That Will Make The Tree Of Opposite Has Only One Node.(i.e)
------ Left Insert Approach ---------- It's Direct Opposite Is Right Insert Approach.
            10
          /    \
        20     30
      /   \
    40     50

DELETION Of General Binary Tree Is As Same As Binary Search Tree (BST). Hence, Deletion In General Binary Tree Is Skipped.
'''
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value,traveler):
        if self.root is None:
            self.root = Node(value)
        if traveler == None:
            traveler = self.root
        elif traveler.left == None:
            traveler.left = Node(value)
        elif traveler.right == None:
            traveler.right = Node(value)
        else:
            self.insert(value,traveler.left)
    def preorder(self,traveler):
        if self.root == None:
            print("Tree Is Empty..!")
        else:
            if not traveler: return
            print(traveler.value,end=" ")
            self.preorder(traveler.left)
            self.preorder(traveler.right)
    def inorder(self,traveler):
        if self.root == None:
            print("Tree Is Empty..!")
        else:
            if not traveler: return
            self.inorder(traveler.left)
            print(traveler.value,end=" ")
            self.inorder(traveler.right)
    def postorder(self,traveler):
        if self.root == None:
            print("Tree Is Empty..!")
        else:
            if not traveler: return
            self.postorder(traveler.left)
            self.postorder(traveler.right)
            print(traveler.value,end=" ")
binaryTree = BinaryTree()
while 1:
    print("\n\n--------- Binary Tree ---------\n1) Insertion\n2) Pre-order Traversal \n3) In-order Traversal\n4) Post-order Traversal\n0) Exit\n\n")
    action = int(input("Enter Number To Take Action: ")) 
    if action == 1:
        binaryTree.insert(int(input("Enter The Value To Be Inserted: ")),binaryTree.root)
        print("\nElement Inserted Successfully..!")
    elif action == 2:
        print('\n--------- Pre-order Traversal---------')
        binaryTree.preorder(binaryTree.root)
    elif action == 3:
        print('\n--------- In-order Traversal---------')
        binaryTree.inorder(binaryTree.root)
    elif action == 4:
        print('\n--------- Post-order Traversal---------')
        binaryTree.postorder(binaryTree.root)
    elif action == 0:
        print("Exiting...")
        exit()
    else:
        print("\nInvalid Input. Enter A Valid Input..!")

'''
----------- TERMINAL RUN OF INPUT/OUTPUT PROCESS -----------

--------- Binary Tree ---------
1) Insertion
2) Pre-order Traversal 
3) In-order Traversal
4) Post-order Traversal
0) Exit


Enter Number To Take Action: 1
Enter The Value To Be Inserted: 10

Element Inserted Successfully..!


--------- Binary Tree ---------
1) Insertion
2) Pre-order Traversal 
3) In-order Traversal
4) Post-order Traversal
0) Exit


Enter Number To Take Action: 1
Enter The Value To Be Inserted: 20

Element Inserted Successfully..!


--------- Binary Tree ---------
1) Insertion
2) Pre-order Traversal 
3) In-order Traversal
4) Post-order Traversal
0) Exit


Enter Number To Take Action: 1
Enter The Value To Be Inserted: 30

Element Inserted Successfully..!


--------- Binary Tree ---------
1) Insertion
2) Pre-order Traversal
3) In-order Traversal
4) Post-order Traversal
0) Exit


Enter Number To Take Action: 1
Enter The Value To Be Inserted: 40

Element Inserted Successfully..!


--------- Binary Tree ---------
1) Insertion
2) Pre-order Traversal
3) In-order Traversal
4) Post-order Traversal
0) Exit


Enter Number To Take Action: 2

--------- Pre-order Traversal---------
10 20 40 30

--------- Binary Tree ---------
1) Insertion
2) Pre-order Traversal
3) In-order Traversal
4) Post-order Traversal
0) Exit


Enter Number To Take Action: 3

--------- In-order Traversal---------
40 20 10 30

--------- Binary Tree ---------
1) Insertion
2) Pre-order Traversal
3) In-order Traversal
4) Post-order Traversal
0) Exit


Enter Number To Take Action: 4

--------- Post-order Traversal---------
40 20 30 10

--------- Binary Tree ---------
1) Insertion
2) Pre-order Traversal
3) In-order Traversal
4) Post-order Traversal
0) Exit


Enter Number To Take Action: 0
Exiting...
'''
