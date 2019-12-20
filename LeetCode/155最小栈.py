import heapq


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.heap = []
        heapq.heapify(self.heap)

    def push(self, x: int) -> None:
        self.stack.append(x)
        heapq.heappush(self.heap, x)

    def pop(self) -> None:
        if self.stack:
            top = self.stack.pop()
            self.heap.remove(top)
            heapq.heapify(self.heap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return heapq.nsmallest(1, self.heap)[0]


class MinStack2:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.helper = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.helper or x < self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.helper.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helper[-1]


if __name__ == '__main__':
    s = MinStack2()
    s.push(3)
    s.push(2)
    s.push(4)
    print(s.stack,s.helper)
    print(s.getMin())
    s.pop()
    s.pop()
    print(s.stack,s.helper)

    print(s.getMin())
