from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i
        if j >= 0 and nums[j] != target:
            return 0
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] >= target:
                j = m - 1
            else:
                i = m + 1
        left = j
        return right - left - 1
