class Solution:
    def myAtoi(self, s: str) -> int:
        tmp = s.replace(" ", "")
        negative = None
        ans = ""
        if tmp[0] == "-":
            negative = True
            tmp = tmp[1:]
        for i in tmp:
            if negative is None and i == "+":
                negative = False
            elif i.isdigit():
                ans += i
            else:
                break
        if not ans:
            return 0
        ret = int(ans)
        if negative:
            ret = ret * -1
            return max(ret, -2 ** 31)
        return min(2 ** 31 - 1, ret)
