class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            sum = max = nums[0]
            for i in range(1, len(nums)):
                if sum >= 0:
                    sum += nums[i]
                else:
                    sum = nums[i]
                if max < sum:
                    max = sum
            return max

