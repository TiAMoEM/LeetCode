class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum1 = n * (n + 1) / 2
        sum2 = 0
        for i in nums:
            sum2 += i
        return int(sum1 - sum2)