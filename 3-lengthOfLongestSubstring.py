class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest, left = 0, 0
        tmp = {}
        for index, each in enumerate(s):
            if each not in tmp or tmp[each] < left:
                longest = max(longest, index - left + 1)
            else:
                left = tmp[each]
            tmp[each] = index + 1
        return longest