class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        ans = ""
        for i in range(len(arr)):
            ans += arr[i][::-1]
            ans += " "
        return ans[:-1]
