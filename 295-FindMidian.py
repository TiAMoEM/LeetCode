class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.arr.append(num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        self.arr.sort()
        if len(self.arr) % 2 == 1:
            return self.arr[len(self.arr) // 2 + 1]
        else:
            return (self.arr[len(self.arr) // 2] + self.arr[len(self.arr) // 2 + 1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


