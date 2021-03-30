class Solution:
    def convertToBase7(self, num: int) -> str:
        tmp = ""
        if num > 0:
            while num // 7 > 0:
                tmp += str(num % 7)
                num = num // 7
            tmp += str(num)
            ans = tmp[::-1]
        else:
            num = num * -1
            while num // 7 > 0:
                tmp += str(num % 7)
                num = num // 7
            tmp += str(num)
            ans = "-" + tmp[::-1]
        return ans
