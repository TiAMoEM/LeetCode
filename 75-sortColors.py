class Solution:
    # 投机取巧的做法
    def sortColors1(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

    def sortColors(self, nums):
        """
        双指针法，三路快排
        :param nums:
        :return:
        """
        i, red, blue = 0, -1, len(nums)
        while i < blue:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                red += 1
                nums[i], nums[red] = nums[red], nums[i]
                i += 1
            else:
                blue -= 1
                nums[i], nums[blue] = nums[blue], nums[i]
