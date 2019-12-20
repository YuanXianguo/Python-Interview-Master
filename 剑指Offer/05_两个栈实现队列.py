class StackToQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, elem):
        self.stack1.append(elem)

    def pop(self):
        if self.stack2:  # 堆栈2不空
            return self.stack2.pop()
        elif not self.stack1:  # 堆栈1，2都空
            return
        else:  # 堆栈1不空
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def pop2(self):
        if not self.stack1 and not self.stack2:  # 堆栈1，2都空
            return
        elif not self.stack2:  # 堆栈2空，1不空
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


if __name__ == '__main__':
    q = StackToQueue()
    for i in range(5):
        q.push(i)
    print(q.stack1, q.stack2)
    print(q.pop(), end=" ")
    print(q.stack1, q.stack2)

    for i in range(5, 10):
        q.push(i)
    print(q.stack1, q.stack2)

    for i in range(10):
        print(q.pop(), end=" ")
        print(q.stack1, q.stack2)

    for i in range(5):
        q.push(i)
    for i in range(5):
        print(q.pop2(), end=" ")

