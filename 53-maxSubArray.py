from typing import List


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            sum1 = max1 = nums[0]
            for i in range(1, len(nums)):
                if sum1 >= 0:
                    sum1 += nums[i]
                else:
                    sum1 = nums[i]
                if max1 < sum1:
                    max1 = sum1
            return max1

    def maxSubArray2(self, nums: List) -> List:
        """
        作业帮面试题：
        返回的是最大的子序列，不只是需要求得最大值
        :param nums:
        :return:
        """
        result = tmp = nums[0]
        start, end = 0, 0
        for i in range(1, len(nums)):
            if tmp > 0:
                tmp += nums[i]
            else:
                tmp = nums[i]
                start = i
            if result < tmp:
                result = tmp
                end = i
        return nums[start: end + 1]
