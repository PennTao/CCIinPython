# Imagine you are reading in a stream of integers. Periodically, you wish to be
# able to look up the rank of a number x(the # of values less than or equal to x)
# Implement the data structures and algorithms to support these operations.
from Tree import *
class IntegerStream:
    def __init__(self):
        self.root = None

    def track(self,x):
        print x
        self.insert(x,self.root)
        

    def insert(self,x,root):
        if root == None :
            root = TreeNode(x)
        elif x <= root.data:
            root.leftchildren = root.leftchildren + 1
            if(root.left == None):               
                root.left = TreeNode(x)
            else:
                self.insert(x,root.left)
        else:
            if(root.right == None):
                root.right = TreeNode(x)
            else:
                self.insert(x,root.right)
        
    def getRankOfNumber(self,x):
        return self.getRank(x,self.root)

    def getRank(self,x,root):
        if root == None:
            return -1
        rank = 0
        if x >root.data:
            return self.getRank(x,root.right) + root.leftchildren
        elif x < root.data:
            return self.getRank(x,root.left)
        else:
            return root.leftchildren
            
