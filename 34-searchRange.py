class Solution:
    def searchRange(self, nums, target: int):
        """

        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums) - 1
        ans = []
        low = 0
        high = 0
        if target not in nums:
            return [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                low = mid
                high = mid
                left = right + 1
        while low != 0 and nums[low - 1] == target:
            low -= 1
        while high != len(nums) - 1 and nums[high + 1] == target:
            high += 1
        ans.append(low)
        ans.append(high)
        return ans
