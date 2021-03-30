from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        ans = 0
        l = 0
        r = 0
        while r < len(nums) - 1:
            if nums[r] < nums[r + 1]:
                r += 1
            else:
                ans = max(ans, r - l + 1)
                l = r + 1
                r += 1
            ans = max(ans, r - l + 1)
        return ans
