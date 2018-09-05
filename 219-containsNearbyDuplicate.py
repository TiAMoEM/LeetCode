class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 暴力遍历求法，LeetCode超时
        # if nums == []:
        #     return False
        # if len(nums) <= k:
        #     for i in range(len(nums)):
        #         for j in range(i + 1, len(nums)):
        #             if nums[j] == nums[i]:
        #                 return True
        #     return False
        # else:
        #     for i in range(len(nums) - k):
        #         for j in range(i + 1, i + k + 1):
        #             if nums[j] == nums[i]:
        #                 return True
        #     for i in range(len(nums) - k, len(nums) - 1):
        #         for j in range(i + 1, len(nums)):
        #             if nums[j] == nums[i]:
        #                 return True
        #     return False

        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                if -k <= i - d[nums[i]] <= k:
                    return True
                else:
                    d[nums[i]] = i
            d[nums[i]] = i
        return False