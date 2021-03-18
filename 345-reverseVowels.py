class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s) - 1
        strlist = list(s)
        while left < right:
            if strlist[left] in vowels:
                if strlist[right] in vowels:
                    strlist[left], strlist[right] = strlist[right], strlist[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                if strlist[right] in vowels:
                    left += 1
                else:
                    left += 1
                    right -= 1
        ans = "".join(strlist)
        return ans
