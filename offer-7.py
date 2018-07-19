# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        if number < 3:
            return number
        a, b, ans = 1, 2, 0
        for i in range(3, number + 1):
            ans = a + b
            a = b
            b = ans
        return ans
