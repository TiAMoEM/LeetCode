from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        return self.verify(postorder, 0, len(postorder) - 1)

    def verify(self, postorder: List[int], left, right) -> bool:
        if left >= right:
            return True
        start = left
        while postorder[start] < postorder[right]:
            start += 1

        index = start
        while postorder[index] > postorder[right]:
            index += 1
        return index == right and self.verify(postorder, left, start - 1) and self.verify(postorder, start, right - 1)
