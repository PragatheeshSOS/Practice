# Adelson Velsky and Landis Tree [AVL Tree].......................................
class Node:
    def __init__(self,value):
        self.value = value
        self.right = self.left = None
class AVL:
    def __init__(self):
        self.root = None
    def insert(self,value,root):
        if root is None:
            return Node(value)
        elif root.value>value:
            root.left = self.insert(value,root.left)
        elif root.value<value:
            root.right = self.insert(value,root.right)
        return self.rebalance(value,root)
    def deletion(self,target,root):
        if root is None:
            print("\n\nTree Is Empty..!")
        elif target>root.value:
            root.right = self.deletion(target,root.right)
        elif target<root.value:
            root.left = self.deletion(target,root.left)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                traveler = root.right
                while traveler.left:
                    traveler = traveler.left
                root.value = traveler.value
                root.right = self.deletion(traveler.value,root.right)
        return self.rebalance(target,root)
    def rebalance(self,value,root):
        balance = self.height(root.left)-self.height(root.right)
        if balance>1:
            if root.left.value>value:
                root = self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                root = self.rightRotate(root)
        elif balance<-1:
            if root.right.value<value:
                root = self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                root = self.leftRotate(root)
        return root
    def rightRotate(self,root):
        top,mid = root,root.left
        temp = mid.right
        mid.right = top
        top.left = temp
        return mid
    def leftRotate(self,root):
        top,mid = root,root.right
        temp = mid.left
        mid.left = top
        top.right = temp
        return mid
    def height(self,root):
        return 1+max(self.height(root.left),self.height(root.right)) if root else 0
    def search(self,target,root):
        if root is None:
            return False
        if target>root.value:
            return self.search(target,root.right)
        elif target<root.value:
            return self.search(target,root.left)
        else:
            return True
    def MinMax(self,root):
        if self.root is None:
            return None,None
        def mini(root):
            if root.left:
                return mini(root.left)
            return root.value
        def maxi(root):
            if root.right:
                return maxi(root.right)
            return root.value
        return mini(root),maxi(root)
    def preorder(self,root):
        if root is None: return
        print(root.value,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    def inorder(self,root):
        if root is None: return
        self.inorder(root.left)
        print(root.value,end=" ")
        self.inorder(root.right)
    def postorder(self,root):
        if root is None: return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.value,end=" ")
    def levelorder(self,root):
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.value, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
avl = AVL()
while True:
    print("\n\n-------- AVL Tree --------")
    print("1) Insertion")
    print("2) Deletion")
    print("3) Height")
    print("4) Balance Factor")
    print("5) Search")
    print("6) Minimum And Maximum")
    print("7) Pre-order Traversal")
    print("8) In-order Traversal")
    print("9) Post-order Traversal")
    print("10) Level-Order Traversal")
    print("0) Exit")
    action = int(input("Enter Action: "))
    if action == 1:
        avl.root = avl.insert(int(input("Enter Value To Be Inserted: ")),avl.root)
        print("\n\nElement Inserted Successfully..!")
    elif action == 2:
        avl.root = avl.deletion(int(input("Enter Target Element To Be Deleted: ")),avl.root)
        print("\n\nElement Deleted Successfully..!")
    elif action == 3:
        print("\n\nHeight: ",avl.height(avl.root))
    elif action == 4:
        print("\n\nBalance Factor: ",avl.height(avl.root.left)-avl.height(avl.root.right))
    elif action == 5:
        print("\n\nSearch Element Exists..!") if avl.search(int(input("Enter Target: ")),avl.root) else print("\n\nSearch Element Doesn't Exists..!")
    elif action == 6:
        minimum,maximum = avl.MinMax(avl.root)
        print(f"\n\nMinimum Element: {minimum}\nMaximum Element: {maximum}")
    elif action == 7:
        print("\n\n-------- Pre-order Traversal --------")
        avl.preorder(avl.root) if avl.root else print("\n\nTree Is Empty..!")
    elif action == 8:
        print("\n\n-------- In-order Traversal --------")
        avl.inorder(avl.root) if avl.root else print("\n\nTree Is Empty..!")
    elif action == 9:
        print("\n\n-------- Post-order Traversal --------")
        avl.postorder(avl.root) if avl.root else print("\n\nTree Is Empty..!")
    elif action == 10:
        avl.levelorder(avl.root) if avl.root else print("\n\nTree Is Empty..!")
    elif action == 0:
        print("\nExiting..!")
        exit()
    else:
        print("\n\nInvalid Action..!")
