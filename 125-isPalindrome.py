class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str1 = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                str1 += i
        str1 = str1.lower()
        str2 = str1[::-1]
        if str2 == str1:
            return True
        else:
            return False