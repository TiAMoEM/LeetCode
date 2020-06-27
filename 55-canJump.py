class Solution:
    def canJump(self, nums) -> bool:
        if 0 not in nums:
            return True
        if len(nums) < 2:
            return True
        max_distance = nums[0]
        for i in range(1, len(nums) - 1):
            if i <= max_distance:
                max_distance = max(max_distance, i + nums[i])
            else:
                break
        return max_distance >= nums[len(nums) - 1]
