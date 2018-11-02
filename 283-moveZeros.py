class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 0
        for num in nums:
            if num != 0:
                nums[k] = num
                k += 1
        nums[k::] = [0] * (len(nums) - k)
        # return nums
