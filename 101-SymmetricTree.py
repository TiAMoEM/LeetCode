# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        else:
            return self.Sym(root.left, root.right)

    def Sym(self, left: TreeNode, right: TreeNode):
        if left == None and right == None:
                return True
        elif left == None or right == None:
            return False
        else:
            if left.val != right.val:
                return False
            return self.Sym(left.left, right.right) and self.Sym(left.right, right.left)