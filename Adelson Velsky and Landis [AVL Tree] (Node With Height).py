# Adelson Velsky and Landis [AVL Tree] (Node With Height)..................................
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None
    
    ''' Insertion Function '''
    def insertion(self,value,root):
        if not root: return Node(value)
        elif value<root.value:
            root.left = self.insertion(value,root.left)
        elif value>root.value:
            root.right = self.insertion(value,root.right)
        self.update_height(root)
        return self.rebalance(root)
    
    ''' Deletion Function'''
    def deletion(self,value,root):
        if not root: return
        elif value<root.value:
            root.left = self.deletion(value,root.left)
        elif value>root.value:
            root.right = self.deletion(value,root.right)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.value = temp.value
                root.right = self.deletion(temp.value,root.right)
        self.update_height(root)
        return self.rebalance(root)
    
    ''' Search '''
    def search(self,value,root):
        if not root:
            return "\n\nSearch Element Doesn't Exists...!" if self.root else "\n\nTree Is Empty...!"
        elif value<root.value:
            return self.search(value,root.left)
        elif value>root.value:
            return self.search(value,root.right)
        return "\n\nSearch Element Exists...!"

    ''' Minimum And Maximum '''
    def MinMax(self,root):
        def minimum(root):
            return minimum(root.left) if root.left else root.value
        def maximum(root):
            return maximum(root.right) if root.right else root.value
        return f"\n\nMinimum: {minimum(root)}\nMaximum: {maximum(root)}"
    
    ''' Number Of Nodes '''
    def no_of_nodes(self,root):
        if not root: return 0
        return 1+self.no_of_nodes(root.left)+self.no_of_nodes(root.right)
    
    ''' Longest Common Ancestor '''
    def LCA(self,root,node1,node2):
        if not root:
            return "\n\nNo Common Ancestor Found...!"
        if node1<root.value and node2<root.value:
            return self.LCA(root.left,node1,node2)
        elif node1>root.value and node2>root.value:
            return self.LCA(root.right,node1,node2)
        return f"\n\nCommon Ancestor: {root.value}"

    '''  Height Updation '''
    def height(self,root):
        return root.height if root else 0
    def update_height(self,root):
        root.height = 1+max(self.height(root.left),self.height(root.right))
    
    ''' Balance Factor '''
    def balance_factor(self,root):
        return self.height(root.left)-self.height(root.right)

    ''' Rebalance Function '''
    def rebalance(self,root):
        balance = self.balance_factor(root)
        
        # Left Left Case
        if balance>1 and self.balance_factor(root.left)>=0:
            return self.rightrotate(root)
        
        # Left Right Case
        elif balance>1:
            root.left = self.leftrotate(root.left)
            return self.rightrotate(root)
        
        # Right Right Case
        if balance<-1 and self.balance_factor(root.right)<=0:
            return self.leftrotate(root)        
        
        # Right Left Case
        elif balance<-1:
            root.right = self.rightrotate(root.right)
            return self.leftrotate(root)
        return root

    ''' Rotations '''
    # Right Rotation
    def rightrotate(self,root):
        top,mid = root,root.left
        temp = mid.right
        mid.right = top
        top.left = temp
        self.update_height(top)
        self.update_height(mid)
        return mid

    # Left Rotation
    def leftrotate(self,root):
        top,mid = root,root.right
        temp = mid.left
        mid.left = top
        top.right = temp
        self.update_height(top)
        self.update_height(mid)
        return mid

    ''' Traversals '''
    # Pre-Order
    def preorder(self,root):
        if not root: return
        print(root.value,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    
    # In-Order
    def inorder(self,root):
        if not root: return
        self.inorder(root.left)
        print(root.value,end=" ")
        self.inorder(root.right)

    # Post-Order
    def postorder(self,root):
        if not root: return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value,end=" ")

    # Level-Order
    def levelorder(self,root):
        queue = [root]
        while queue:
            popping = queue.pop(0)
            print(popping.value,end=' ')
            if popping.left:
                queue.append(popping.left)
            if popping.right:
                queue.append(popping.right)

''' Main Function '''
avltree = AVL()
while True:
    print('\n\n ------------- AVL Tree -------------')
    print("\n -------- Actions --------")
    print('1) Insertion')
    print('2) Deletion')
    print('3) Search')
    print('4) Traversal')
    print('5) Minimum And Maximum')
    print('6) LCA')
    print('7) Height Of Tree')
    print('8) Balance Factor')
    print('9) Number Of Nodes')
    print('0) Exit')

    action = int(input("Enter Action: "))
    
    if action == 1:
        avltree.root = avltree.insertion(int(input("Enter Value To Be Inserted: ")),avltree.root)
        print("\n\nElement Inserted Successfully...!")
        
    elif action == 2:
        if not avltree.root:
            print("\n\nTree Is Empty...!")
        else:
            avltree.root = avltree.deletion(int(input("Enter Value To Be Deleted: ")),avltree.root)
            print("\n\nElement Deleted Successfully...!")

    elif action == 3:
        print(avltree.search(int(input("Enter Searching Value: ")), avltree.root))
    
    elif action == 4:
        if not avltree.root:
            print("\n\nTree Is Empty..!")
        else:
            print("\n\n --------------- Traversals ---------------")
            print("\n\n -------- Pre-Order Traversal --------")
            avltree.preorder(avltree.root)
            
            print("\n\n -------- In-Order Traversal --------")
            avltree.inorder(avltree.root)
            
            print("\n\n -------- Post-Order Traversal --------")
            avltree.postorder(avltree.root)
            
            print("\n\n -------- Level-Order Traversal --------")
            avltree.levelorder(avltree.root)
    
    elif action == 5:
        print(avltree.MinMax(avltree.root)) if avltree.root else print("\n\nTree Is Empty...!")
    
    elif action == 6:
        if avltree.root:
            print(avltree.LCA(avltree.root,int(input("Enter First Node: ")),int(input("Enter Second Node: "))))
        else:
            print("\n\nTree Is Empty...!")

    elif action == 7:
        print(f"\n\nHeight Of Tree: {avltree.height(avltree.root)}") if avltree.root else print("\n\nTree Is Empty...!")
    
    elif action == 8:
        print(f"\n\nBalance Factor: {avltree.balance_factor(avltree.root)}") if avltree.root else print("\n\nTree Is Empty...!")

    elif action == 9:
        print("\n\nNumber Of Nodes: ",avltree.no_of_nodes(avltree.root))

    elif action == 0:
        print("Exiting...!")
        exit()
    else:
        print("\n\nEnter Valid Action...!")

'''
------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 4


Tree Is Empty..!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 1
Enter Value To Be Inserted: 10


Element Inserted Successfully...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 4


--------------- Traversals ---------------


-------- Pre-Order Traversal --------
10

-------- In-Order Traversal --------
10

-------- Post-Order Traversal --------
10

-------- Level-Order Traversal --------
10

------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 2
Enter Value To Be Deleted: 10


Element Deleted Successfully...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 4


Tree Is Empty..!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 1
Enter Value To Be Inserted: 10


Element Inserted Successfully...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 5


Minimum: 10
Maximum: 10


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 2
Enter Value To Be Deleted: 10


Element Deleted Successfully...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 4


Tree Is Empty..!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 1
Enter Value To Be Inserted: 10 


Element Inserted Successfully...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 1
Enter Value To Be Inserted: 5


Element Inserted Successfully...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 1
Enter Value To Be Inserted: 2


Element Inserted Successfully...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 8


Balance Factor: 0


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 7


Height Of Tree: 2


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 3
Enter Searching Value: 5


Search Element Exists...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 3
Enter Searching Value: 6


Search Element Doesn't Exists...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 6
Enter First Node: 5
Enter Second Node: 10


Common Ancestor: 5


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 5


Minimum: 2
Maximum: 10


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 4


--------------- Traversals ---------------


-------- Pre-Order Traversal --------
5 2 10

-------- In-Order Traversal --------
2 5 10

-------- Post-Order Traversal --------
2 10 5

-------- Level-Order Traversal --------
5 2 10

------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 7


Height Of Tree: 2


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 9


Number Of Nodes:  3


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 1
Enter Value To Be Inserted: 15


Element Inserted Successfully...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 1
Enter Value To Be Inserted: 20


Element Inserted Successfully...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 1
Enter Value To Be Inserted: 25


Element Inserted Successfully...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 4


--------------- Traversals ---------------


-------- Pre-Order Traversal --------
15 5 2 10 20 25

-------- In-Order Traversal --------
2 5 10 15 20 25

-------- Post-Order Traversal --------
2 10 5 25 20 15

-------- Level-Order Traversal --------
15 5 20 2 10 25

------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 2
Enter Value To Be Deleted: 25


Element Deleted Successfully...!


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 9


Number Of Nodes:  5


------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 4


--------------- Traversals ---------------


-------- Pre-Order Traversal --------
15 5 2 10 20

-------- In-Order Traversal --------
2 5 10 15 20

-------- Post-Order Traversal --------
2 10 5 20 15

-------- Level-Order Traversal --------
15 5 20 2 10

------------- AVL Tree -------------

-------- Actions --------
1) Insertion
2) Deletion
3) Search
4) Traversal
5) Minimum And Maximum
6) LCA
7) Height Of Tree
8) Balance Factor
9) Number Of Nodes
0) Exit
Enter Action: 0
Exiting...!
'''
