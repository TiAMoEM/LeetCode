class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = 0
        for i in range(len(s) - 1):
            c = s[i]
            cafter = s[i + 1]
            if dic[c] < dic[cafter]:
                ans -= dic[c]
            else:
                ans += dic[c]
        ans += dic[s[-1]]
        return ans