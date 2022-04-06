# -*- coding:utf-8 -*-

class CQueue:

    def __init__(self):
        self.arr1 = []
        self.arr2 = []

    def appendTail(self, value: int) -> None:
        self.arr1.append(value)

    def deleteHead(self) -> int:
        if self.arr2:
            return self.arr2.pop()
        if not self.arr1:
            return -1

        while self.arr1:
            self.arr2.append(self.arr1.pop())

        return self.arr2.pop()
