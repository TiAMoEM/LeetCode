# -*- coding:utf-8 -*-
import math
class Solution:
    def jumpFloorII(self, number):
        if number == 1:
            return number
        ans = math.pow(2, number - 1)
        return ans