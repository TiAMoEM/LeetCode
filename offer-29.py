# -*- coding:utf-8 -*-
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) < k:
            return []
        return heapq.nsmallest(k, tinput)

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        