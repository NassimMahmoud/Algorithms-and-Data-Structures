
class BinarySearchTree:
    
    def __init__(self, val=None):
        # Initialize the BinarySearchTree node with a value
        self.value = val
        # Create left and right child nodes 
        #if the value is not None
        if self.value:
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        else:
            self.left = None
            self.right = None
            

    def isempty(self):
        # Check if the node is empty (value is None)
        return (self.value == None)

    def insert(self, data):
        # Insert a new value into the BinarySearchTree
        if self.isempty():
            self.value = data
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        elif self.value == data:
            return
        elif data < self.value:
            self.left.insert(data)
            return
        elif data > self.value:
            self.right.insert(data)
            return

    def isleaf(self):
        # Check if the node is a leaf node (no children)
        if self.left == None and self.right == None:
            return True
        else:
            return False

    def maxval(self):
        # Find the maximum value in the BinarySearchTree
        if self.right.right == None:
            return (self.value)
        else:
            return (self.right.maxval())
        
    def minval(self):
         # Find the maximum value in the BinarySearchTree
        if self.left.left == None:
            return (self.value)
        else:
            return (self.left.minval())
        

    def delete(self, v):
        # Delete a value from the BinarySearchTree
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v == self.value:
            if self.isleaf():
                self.value = None
                self.left =  None
                self.right = None
                return
            elif self.left.isempty():
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return
            else:
                
                #replace the value with the min value in the right tree
                self.value = self.right.minval()
                
                #reimplement the deletation process on self.right
                self.right.delete(self.right.value)
                return

    def inorder(self):
        # Traverse the BinarySearchTree in inorder (left-root-right) 
        #and return the values
        if self.isempty():
            return ([])
        else:
            return (self.left.inorder() + [self.value] + self.right.inorder())
        
    def preorder(self):
        # Traverse the BinarySearchTree in inorder (left-root-right) 
        #and return the values
        if self.isempty():
            return ([])
        else:
            return ([self.value] + self.left.preorder() + self.right.preorder())
        
    def postorder(self):
        # Traverse the BinarySearchTree in inorder (left-root-right) 
        #and return the values
        if self.isempty():
            return ([])
        else:
            return (self.left.postorder() + self.right.postorder()+[self.value] )
        
    

# Test the BinarySearchTree class
t = BinarySearchTree(5)








