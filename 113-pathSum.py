# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, res, [])
        return res

    def dfs(self, root, sum, res, path):
        if root is None:
            return
        if root.left is None and root.right is None:
            if sum == root.val:
                res.append(path + [root.val])

        self.dfs(root.left, sum - root.val, res, path + [root.val])
        self.dfs(root.right, sum - root.val, res, path + [root.val])
