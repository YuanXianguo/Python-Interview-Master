"""题目：输入一个链表，从尾到头打印链表每个节点的值。"""


class Node(object):
    def __init__(self, elem=None, node=None):
        self.next = node
        self.elem = elem


class SingleLinkList(object):
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return not self.head

    def get_length(self):
        cursor = self.head
        count = 0
        while cursor:
            cursor = cursor.next
            count += 1
        return count

    def travel(self):
        cursor = self.head
        while cursor:
            print(cursor.elem, end=" ")
            cursor = cursor.next
        print("")

    def travel_reverse(self):
        stack = []
        cursor = self.head
        while cursor:
            stack.append(cursor)
            cursor = cursor.next
        while stack:
            print(stack.pop().elem, end=" ")
        print("")

    def add_front(self, elem):
        """头插"""
        node = Node(elem)
        node.next = self.head
        self.head = node

    def add_rear(self, elem):
        """尾插"""
        node = Node(elem)
        cursor = self.head
        if not cursor:
            self.head = node
        else:
            while cursor.next:
                cursor = cursor.next
            cursor.next = node

    def insert(self, index, elem):
        """指定位置插入"""
        node = Node(elem)
        if index <= 0:
            self.add_front(elem)
        elif index >= self.get_length():
            self.add_rear(elem)
        else:
            pre = self.head
            cnt = 0
            while cnt < index - 1:
                pre = pre.next
                cnt += 1
            node.next = pre.next
            pre.next = node

    def remove(self, elem):
        """删除第一个指定元素"""
        cursor = self.head
        pre = None
        while cursor:
            if cursor.elem == elem:
                if cursor == self.head:
                    self.head = cursor.next
                else:
                    pre.next = cursor.next
                return "删除成功"
            else:
                pre = cursor
                cursor = cursor.next
        return "删除失败"

    def search(self, elem):
        """查找指定元素是否在链表中"""
        cursor = self.head
        while cursor:
            if cursor.elem == elem:
                return True
            else:
                cursor = cursor.next
        return False


if __name__ == '__main__':
    sll = SingleLinkList()
    print(sll.is_empty())
    sll.add_rear("尾")
    sll.add_front("头")

    for i in range(1, 10):
        sll.insert(i, i)
    sll.travel()
    sll.travel_reverse()
