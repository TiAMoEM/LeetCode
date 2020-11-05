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
