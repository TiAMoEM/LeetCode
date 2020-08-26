# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode):
        """
        :type root: Tree
        """
        # stack = []
        # if root != None:
        #     stack.append((1, root))
        # depth = 0
        # while stack != []:
        #     currDepth, root = stack.pop()
        #     if root != None:
        #         depth = max(currDepth, depth)
        #         stack.append((currDepth + 1, root.left))
        #         stack.append((currDepth + 1, root.right))
        # return depth

        if not root:
            return 0
        else:
            max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
