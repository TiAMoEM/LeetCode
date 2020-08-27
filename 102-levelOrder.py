# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution:
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     ans = []
    #     if not root:
    #         return ans
    #     temp = [root]
    #     while temp:
    #         son = []
    #         ans.append([node.val for node in temp])
    #         for node in temp:
    #             if node.left:
    #                 son.append(node.left)
    #             if node.right:
    #                 son.append(node.right)
    #         temp = son
    #     return ans

    """
    BFS算法
    """

    def levelOrder(self, root: TreeNode):
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res
