from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        不符合题目要求的时间复杂度的解法
        :param nums1:
        :param nums2:
        :return: 
        """
        arr = nums1 + nums2
        arr.sort()
        size = len(arr)
        if size % 2 == 0:
            ans = (arr[size // 2 - 1] + arr[size // 2]) / 2.0
        else:
            ans = arr[(size - 1) // 2] / 1.0
        return ans

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        length = m + n
        i, j = 0, 0
        left, right = 0, 0

        for k in range(length // 2 + 1):
            left = right
            if i < m and (j >= n or nums1[i] < nums2[j]):
                right = nums1[i]
                i += 1
            else:
                right = nums2[j]
                j += 1

        if length % 2 == 0:
            return (left + right) / 2.0

        return right
