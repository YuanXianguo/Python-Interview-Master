"""
题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""


class RandomListNode(object):
    def __init__(self, elem=None):
        self.label = elem
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return
        head = pHead
        # 在原链表每个结点后面添加一个复制结点
        while head:
            copy_node = RandomListNode(head.label)
            copy_node.next = head.next
            head.next = copy_node

            head = copy_node.next
        # 修改随机结点
        head = pHead
        while head:
            copy_node = head.next
            if head.random is not None:
                copy_node.random = head.random.next

            head = copy_node.next
        # 拆分复制链表
        head = pHead
        copy_head = head.next
        while head:
            copy_node = head.next
            head.next = copy_node.next
            copy_node.next = copy_node.next.next if copy_node.next else None

            head = head.next
        return copy_head


def clone(pHead):
    if not pHead:
        return

    # 在每个结点后面添加一个复制的结点
    head = pHead
    while head:
        copy = RandomListNode(head.label)
        copy.next = head.next
        head.next = copy

        head = copy.next  # 遍历

    # 修改随机指针
    head = pHead
    while head:
        copy = head.next
        if head.random is not None:
            copy.random = head.random.next

        head = copy.next

    # 分离复制链表
    head = pHead
    tmp = copy = head.next
    head.next = copy.next
    head = head.next

    while head:
        copy.next = head.next
        copy = copy.next
        head.next = copy.next
        head = head.next

    return tmp


def clone2(pHead):
    if not pHead:
        return
    # 插入复制结点
    head = pHead
    while head:
        copy = RandomListNode(head.label)
        copy.next = head.next
        head.next = copy

        head = copy.next

    # 修改随机指针
    head = pHead
    while head:
        copy = head.next
        if head.random:
            copy.random = head.random.next

        head = copy.next

    # 分离
    head = pHead
    dummy = pHead.next
    while head:
        copy = head.next
        head.next = copy.next
        if head.next:
            copy.next = head.next.next
        else:
            copy.next = None
        head = head.next
    return dummy


if __name__ == '__main__':
    head = RandomListNode(1)
    node1 = RandomListNode(2)
    node2 = RandomListNode(3)
    head.next = node1
    head.random = node2
    node1.next = node2
    node1.random = head

    clone_head = clone(head)
    s = Solution()
    # clone_head = s.Clone(head)
    while clone_head:

        print(clone_head.label, clone_head.random)
        clone_head = clone_head.next
