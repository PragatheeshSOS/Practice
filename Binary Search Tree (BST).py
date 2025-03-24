#Binary Search Tree (BST)
class Node:
    def __init__(self,value):
        self.value = value
        self.left = self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,value,traveler):
        if self.root is None:
            self.root = Node(value)
            return
        if traveler is None:
            traveler = self.root
        elif traveler.value>value:
            if traveler.left is None:
                traveler.left = Node(value)
            else:
                self.insert(value,traveler.left)
        elif traveler.value<value:
            if traveler.right is None:
                traveler.right = Node(value)
            else:
                self.insert(value,traveler.right)
        else:
            print("Element Already Exists..!")
    def delete(self,target,root):
        if root is None:
            print("\n\nTree Is Empty..!")
            return None
        if root.value>target:
            root.left = self.delete(target,root.left)
        elif root.value<target:
            root.right = self.delete(target,root.right)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                traveler = root.right
                while traveler.left is not None:
                    traveler = traveler.left
                root.value = traveler.value
                root.right = self.delete(traveler.value,root.right)
        return root
    def preorder(self,traveler):
        if self.root is None:
            print("\n\nTree Is Empty..!")
            return
        if not traveler: return
        print(traveler.value,end=" ")
        self.preorder(traveler.left)
        self.preorder(traveler.right)
    def inorder(self,traveler):
        if self.root is None:
            print("\n\nTree Is Empty..!")
            return
        if not traveler: return
        self.inorder(traveler.left)
        print(traveler.value,end=" ")
        self.inorder(traveler.right)
    def postorder(self,traveler):
        if self.root is None:
            print("\n\nTree Is Empty..!")
            return
        if not traveler: return
        self.postorder(traveler.left)
        self.postorder(traveler.right)
        print(traveler.value,end=" ")
bstree = BST()
while True:
    print("\n\n\n--------- Binary Search Tree ---------\n1) Insertion\n2) Deletion\n3) Pre-order Traversal\n4) In-order Traversal\n5) Post-order Traversal\n0) Exit\n")
    action = int(input("Enter Number To Take Action: "))
    if action == 1:
        bstree.insert(int(input("Enter Value To Be Inserted: ")),bstree.root)
        print("\n\nElement Inserted Successfully..!")
    elif action == 2:
        bstree.root = bstree.delete(int(input("Enter Target Element To Be Deleted: ")),bstree.root)
        print("\n\nDone Deletion..!")
    elif action == 3:
        print("\n\n--------- Pre-order Traversal ---------")
        bstree.preorder(bstree.root)
    elif action == 4:
        print("\n\n--------- In-order Traversal ---------")
        bstree.inorder(bstree.root)
    elif action == 5:
        print("\n\n--------- Post-order Traversal ---------")
        bstree.postorder(bstree.root)
    elif action == 0:
        print("Exiting..!")
        exit()
    else:
        print("\nEnter A Valid Input..!")
'''
--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 10


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 2
Enter Target Element To Be Deleted: 10


Done Deletion..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 3


--------- Pre-order Traversal ---------


Tree Is Empty..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 10


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 5


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 4


--------- In-order Traversal ---------
5 10


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 3


--------- Pre-order Traversal ---------
10 5


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 5


--------- Post-order Traversal ---------
5 10


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 2
Enter Target Element To Be Deleted: 10


Done Deletion..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 4


--------- In-order Traversal ---------
5


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 4


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 3


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 2


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 6


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 7


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 18

Enter A Valid Input..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 8


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 4


--------- In-order Traversal ---------
2 3 4 5 6 7 8


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 3


--------- Pre-order Traversal ---------
5 4 3 2 6 7 8


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 5


--------- Post-order Traversal ---------
2 3 4 8 7 6 5


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 2
Enter Target Element To Be Deleted: 8


Done Deletion..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 4


--------- In-order Traversal ---------
2 3 4 5 6 7


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 3


--------- Pre-order Traversal ---------
5 4 3 2 6 7


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 2
Enter Target Element To Be Deleted: 6


Done Deletion..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 3


--------- Pre-order Traversal ---------
5 4 3 2 7


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Pre-order Traversal
4) In-order Traversal
5) Post-order Traversal
0) Exit

Enter Number To Take Action: 0
Exiting..!
'''
