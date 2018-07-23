# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        a, b, ans = 1, 2, 0
        if number < 3:
            return number
        else:
            for i in range(3, number + 1):
                ans = a + b
                a = b
                b = ans
            return ans