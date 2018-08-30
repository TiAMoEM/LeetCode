class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        tmp = bin(n)
        s = str(tmp[2:])
        while len(s) < 32:
            s = '0' + s
        arr = []
        a = ''
        for i in s:
            arr.append(i)
        arr.reverse()
        for i in range(len(arr)):
            a += arr[i]
        return int(a, 2)

