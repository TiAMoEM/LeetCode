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

    def moveZeroes2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        双指针法
        """
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == 0:
                if nums[j] == 0:
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1
