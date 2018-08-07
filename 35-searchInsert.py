class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        left = 0
        right = len(nums)
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            if target < nums[0]:
                return 0
            elif target > nums[-1]:
                return len(nums)
            else:
                for i in range(len(nums)):
                    if nums[i] < target and nums[i + 1] > target:
                        return i + 1


