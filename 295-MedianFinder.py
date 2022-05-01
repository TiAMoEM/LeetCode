class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        if not self.arr:
            return float(0)
        length = len(self.arr)
        self.arr.sort()
        if length % 2 == 1:
            return float(self.arr[length // 2])
        else:
            return float((self.arr[length // 2] + self.arr[length // 2 - 1]) / 2)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
