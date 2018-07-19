# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        length = len(rotateArray)
        if length == 0:
            return 0
        # start = 0
        # end = len(rotateArray) - 1
        # result = 0
        for i in range(length):
            if rotateArray[i] > rotateArray[i + 1]:
                return rotateArray[i + 1]

