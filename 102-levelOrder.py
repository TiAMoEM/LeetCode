# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if not root:
            return ret
        temp = [root]
        while temp:
            son = []
            ret.append([node.val for node in temp])
            for node in temp:
                if node.left:
                    son.append(node.left)
                if node.right:
                    son.append(node.right)
            temp = son
        return ret