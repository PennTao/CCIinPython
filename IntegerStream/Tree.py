class TreeNode(object):
    def __init__(self,x):
        self.left = None
        self.right = None
        self.data = x
        self.leftchildren = 0

    def insert(self,data):
        if data <= self.data:
            self.leftchildren = self.leftchildren + 1
            if self.left == None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

