from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        tmp = 1
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            tmp = nums[j + 1] * tmp
            ans[j] *= tmp
        return ans
