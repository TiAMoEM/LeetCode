# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        l1 = []
        l2 = []
        for i in range(len(array)):
            if array[i] % 2 == 1:
                l1.append(array[i])
            else:
                l2.append(array[i])
        return l1 + l2

