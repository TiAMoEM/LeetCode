from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.data) > 1:
            self.queue.append(self.data.popleft())
        ans = self.data.popleft()
        self.data, self.queue = self.queue, self.data
        return ans

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.data[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.data) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
