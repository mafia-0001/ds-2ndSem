class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, x):
        if x < self.val:
            if self.left:
                self.left.insert(x)
            else:
                self.left = BST(x)
        else:
            if self.right:
                self.right.insert(x)
            else:
                self.right = BST(x)

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val, end=" ")
        if self.right:
            self.right.inorder()