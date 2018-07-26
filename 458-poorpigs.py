class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        test = minutesToTest // minutesToDie + 1
        pigs = 0
        while test ** pigs < buckets:
            pigs += 1
        return pigs