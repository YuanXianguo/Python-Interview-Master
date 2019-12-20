"""
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack or node < self.min_stack[-1]:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        # write code here
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.min_stack[-1]


import heapq


class Solution2(object):
    def __init__(self):
        self.stack = []
        self.heap = []
        heapq.heapify(self.heap)

    def push(self, node):
        self.stack.append(node)
        heapq.heappush(self.heap, node)

    def pop(self):
        if not self.stack:
            return
        top = self.stack.pop()
        self.heap.remove(top)
        heapq.heapify(self.heap)

    def min(self):
        return heapq.nsmallest(1, self.heap)[0]


class Solution3(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        self.stack.append(node)
        if not self.min_stack or node < self.min_stack[-1]:
            self.min_stack.append(node)

    def pop(self):
        if not self.stack:
            return
        top = self.stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()
        return top

    def min(self):
        return self.min_stack[-1]


if __name__ == '__main__':
    s = Solution()
    s.push(3)
    print(s.min())
    s.push(4)
    print(s.min())
    s.push(2)
    print(s.min())

