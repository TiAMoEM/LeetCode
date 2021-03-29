from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        ans = 0
        tmp = 0
        while i < len(nums):
            if nums[i] == 1:
                tmp += 1
            else:
                ans = max(ans, tmp)
                tmp = 0
            ans = max(ans, tmp)
            i += 1
        return ans
