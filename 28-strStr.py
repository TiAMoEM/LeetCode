class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        elif needle not in haystack:
            return -1
        elif len(needle) > len(haystack):
            return -1
        else:
            for i in range(len(haystack)):
                k = i
                j = 0
                while j < len(needle) and k < len(haystack) and haystack[k] == needle[j]:
                    j += 1
                    k += 1
                if j == len(needle):
                    return i
            return -1
            