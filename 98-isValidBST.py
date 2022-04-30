# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float('-inf'), float('inf'))

    def isValid(self, root: TreeNode, min_value, max_value):
        if not root:
            return True
        if root.val >= max_value or root.val <= min_value:
            return False
        return self.isValid(root.left, min_value, root.val) and self.isValid(root.right, root.val, max_value)
