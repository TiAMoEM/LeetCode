# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


import collections


class Solution:
    def levelOrder(self, root: 'Node'):
        queue = collections.deque()
        queue.append(root)
        ans = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                if not node:
                    continue
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            if level:
                ans.append(level)
        return ans
