from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag += 1
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return flag <= 1
