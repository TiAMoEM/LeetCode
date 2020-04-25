class Solution(object):
    def rob(self, nums):
        """
        动态规划，dp[0] = 0, dp[1] = nums[1]
        dp[n] = max(dp[n-1], dp[n-2] + nums[n])
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[(i - 1)], dp[(i - 2)] + nums[i])
        return dp[(len(nums) - 1)]
