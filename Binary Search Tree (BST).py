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
    def search(self,target,root):
        if root == None:
            return False
        if root.value == target:
            return True
        if root.value<target:
            return self.search(target,root.right)
        if root.value>target:
            return self.search(target,root.left)
    def height(self,root):
        if root is None:
            return -1
        return 1+ max(self.height(root.left),self.height(root.right))
    def LCA(self,leftvalue,rightvalue,root):
        if root is None:
            return None
        elif leftvalue<root.value and rightvalue<root.value:
            return self.LCA(leftvalue,rightvalue,root.left)
        elif leftvalue>root.value and rightvalue>root.value:
            return self.LCA(leftvalue,rightvalue,root.right)
        else:
            return root
    def minMax(self,root):
        if root is None:
            return None,None
        def mini(root):
            if root.left is not None:
                return mini(root.left)
            return root.value
        def maxi(root):
            if root.right is not None:
                return maxi(root.right)
            return root.value
        return mini(root),maxi(root)
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
    def levelorder(self,traveler):
        if self.root is None:
            print("\n\nTree Is Empty..!")
            return
        else:
            queue = [self.root]
            while queue:
                traveler = queue.pop(0)
                print(traveler.value,end=" ")
                if traveler.left:
                    queue.append(traveler.left)
                if traveler.right:
                    queue.append(traveler.right)
bstree = BST()
while True:
    print("\n\n\n--------- Binary Search Tree ---------\n1) Insertion\n2) Deletion\n3) Search\n4) LCA\n5) Height Of BST\n6) Minimum And Maximum\n7) Pre-order Traversal\n8) In-order Traversal\n9) Post-order Traversal\n10) Level-order Traversal\n0) Exit\n")
    action = int(input("Enter Number To Take Action: "))
    if action == 1:
        bstree.insert(int(input("Enter Value To Be Inserted: ")),bstree.root)
        print("\n\nElement Inserted Successfully..!")
    elif action == 2:
        print("\n!.....DELETION WILL DONE ONLY WHEN TARGET FOUND.....!")
        bstree.root = bstree.delete(int(input("Enter Target Element To Be Deleted: ")),bstree.root)
        print("\n\nTree Is Empty..!") if bstree.root == None else print("\n\nElement Deleted Successfully..!")
    elif action == 3:
        print("\n\nSearch Element Exists..!") if bstree.search(int(input("Enter Search Element: ")),bstree.root) else print("\n\nSearch Element Doesn't Exists..!")
    elif action == 4:
        print("\n\nLongest Common Ancestor Is",bstree.LCA(int(input("Enter Left Node Value: ")),int(input("Enter Right Node Value: ")),bstree.root).value)
    elif action == 5:
        print(f"\n\nHeight Of BST: {bstree.height(bstree.root)}")
    elif action == 6:
        minimum,maximum = bstree.minMax(bstree.root)
        print(f"\n\nMinimum Element Is {minimum}\nMaximum Element Is {maximum}") if maximum is not None and minimum is not None else print("\n\nTree Is Empty")
    elif action == 7:
        print("\n\n--------- Pre-order Traversal ---------")
        bstree.preorder(bstree.root)
    elif action == 8:
        print("\n\n--------- In-order Traversal ---------")
        bstree.inorder(bstree.root)
    elif action == 9:
        print("\n\n--------- Post-order Traversal ---------")
        bstree.postorder(bstree.root)
    elif action == 10:
        print("\n\n--------- Level-order Traversal ---------")
        bstree.levelorder(bstree.root)
    elif action == 0:
        print("Exiting..!")
        exit()
    else:
        print("\nEnter A Valid Input..!")
'''
--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 10


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 5


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 15


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 7


--------- Pre-order Traversal ---------
10 5 15


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 8 


--------- In-order Traversal ---------
5 10 15


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 9


--------- Post-order Traversal ---------
5 15 10


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 1
Enter Value To Be Inserted: 11


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 7


--------- Pre-order Traversal ---------
10 5 15 11


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 2

!.....DELETION WILL DONE ONLY WHEN TARGET FOUND.....!
Enter Target Element To Be Deleted: 11


Element Deleted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 7


--------- Pre-order Traversal ---------
10 5 15


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 6


Minimum Element Is 5
Maximum Element Is 15



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 5


Height Of BST: 1



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 4
Enter Left Node Value: 5
Enter Right Node Value: 15


Longest Common Ancestor Is 10



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 3
Enter Search Element: 12


Search Element Doesn't Exists..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 3
Enter Search Element: 10


Search Element Exists..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
0) Exit

Enter Number To Take Action: 0
Exiting..!
'''

# Level Order Traversal Function Added............
'''

--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
10) Level-order Traversal
0) Exit

Enter Number To Take Action: 
10


--------- Level-order Traversal ---------


Tree Is Empty..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
10) Level-order Traversal
0) Exit

Enter Number To Take Action: 
1
Enter Value To Be Inserted: 
10


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
10) Level-order Traversal
0) Exit

Enter Number To Take Action: 
1
Enter Value To Be Inserted: 
5


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
10) Level-order Traversal
0) Exit

Enter Number To Take Action: 
1
Enter Value To Be Inserted: 
15


Element Inserted Successfully..!



--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
10) Level-order Traversal
0) Exit

Enter Number To Take Action: 
10


--------- Level-order Traversal ---------
10 5 15 


--------- Binary Search Tree ---------
1) Insertion
2) Deletion
3) Search
4) LCA
5) Height Of BST
6) Minimum And Maximum
7) Pre-order Traversal
8) In-order Traversal
9) Post-order Traversal
10) Level-order Traversal
0) Exit

Enter Number To Take Action: 
0
Exiting..!
'''
