class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, num in enumerate(nums):
            dict[num] = i
        for i, num in enumerate(nums):
            if target - nums[i] in dict and dict[target - num] != i:
                return [i, dict[target - num]]