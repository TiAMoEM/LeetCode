class Solution:
    def addDigits(self, num: int) -> int:
        n = sum(int(i) for i in str(num))
        if n < 10:
            return n
        else:
            return self.addDigits(n)
