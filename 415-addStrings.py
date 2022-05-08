class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = ""
        while i >= 0 or j >= 0:
            if i >= 0:
                n1 = int(num1[i])
            else:
                n1 = 0
            if j >= 0:
                n2 = int(num2[j])
            else:
                n2 = 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i -= 1
            j -= 1

        if carry:
            res = "1" + res
        return res
