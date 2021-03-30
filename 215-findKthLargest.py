import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = heapq.nlargest(k, nums)
        return arr[-1]
