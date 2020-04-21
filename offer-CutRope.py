# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        """
        贪婪算法：
        当每一段长为e时会有最大解，因为绳子需要是整数，所以当为2或者3时最大
        但因为number为3时，最大值为2，number为2时，最大值为1
        因此需要尽可能多的3
        :param number: 绳子长度
        :return:
        """
        if number <= 0:
            return 0
        if number == 1 or number == 2:
            return 1
        if number == 3:
            return 2
        m = number % 3
        if m == 0:
            return 3 ** (number // 3)
        elif m == 1:
            return 3 ** (number // 3 - 1) * 4
        else:
            return 3 ** (number // 3) * 2