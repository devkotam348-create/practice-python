##1. Define a class Node with instance variables left, item and right. the variables left and right are used to refer left and right child node _the item variables is
##used to refer left and right child node. The item variable is ude to hold data item

class Node:
    def __init__(self, item = None, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right
        
##2. define a class bst to implement binary search tree data structure. Make __init__()method to create root instance variable to hold the referene of root node

class bst:
    def __init__(self):
        self.root = None
        
##3. in a class bst define insert method to store new data in the binary search tree 
    def is_empty(self):
        return self.root is None
    
    def is_insert(self,data):
        self.root = self.rinsert(self.root, data)
    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data > root.item:
            root.right = self.rinsert(root.right, data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        return root
## in class bst , define a search method to find a giben item in the binary search tree and returns the node reference. It return None if search failed 
    def search(self, data):
       return self.rsearch(self.root,data)
    
    def rsearch(self, root, data):
        if root is None or root.item ==  data:
            return root
        if data > root.item:
            return self.rsearch(root.right, data)
        if data < root.item:
            return self.rsearch(root.left, data)
        
    ## 5. in class bst, define a method to implememnt inorder traversal
    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result
    def rinorder(self, root, result):
        if root:
           self.rinorder(root.left, result)
           result.append(root.item)
           self.rinorder(root.right, result)
    ##6. in classbst , define a method to implement preorder traversal
    def preorder (self):
        result = []
        self.rpreorder(self.root, result)
        return result
    def rpreorder(self, root, result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)
    ##7. in a class bst , define a method to implement psotorder traversal
    def postorder(self):
        result = []
        self.rpostorder(self.root, result)
        return result
    def rpostorder(self, root, result):
        if root:
            self.rpostorder(root.right, result)
            self.rpostorder(root.left, result)
            result.append(root.item)
     ##8. in a class bst , define a method to find mininmum value item node .
    def min_value(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.item
    ##9. in a class bst, define a method to find the maxmimum value item node
    def max_value(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.item
    ## in class bst, define a method to delete a node from binary search tree.
    def is_delete(self, data):
        self.root = self.rdelete (self.root, data)
    def rdelete(self, root , data):
        if root is None:
            return None
        if data < root.item:
            root.left = self.rdelete(root.left, data)
        elif data > root.item:
            root.right = self.rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)
            root.right = self.rdelete(root.right, root.item)
        return root
    ##11. in class bst, define a method size to return a number of elements present in the bst 
    def bst_length(self):
        return len(self.inorder())
    
    

    
e = bst()
e.is_insert(20)
e.is_insert(40)
e.is_insert(10)
e.is_insert(5)
print(e.max_value())    
print(e.min_value())       
         
        
            