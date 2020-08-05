class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = 0
        for i in digits:
            a = a * 10 + i
        b = a + 1
        ans = []
        for i in str(b):
            ans.append(int(i))
        return ans
