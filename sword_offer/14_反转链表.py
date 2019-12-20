"""
题目：输入一个链表，反转链表后，输出链表的所有元素。
"""
from sword_offer.single_link_list import SingleLinkList


def reverse_list(sll):
    if not sll.head:
        return

    # 将链表结点放到堆栈里
    stack = []
    cursor = sll.head
    while cursor:
        stack.append(cursor)
        cursor = cursor.next

    # 反转链表
    sll.head = stack.pop()
    cursor = sll.head
    while stack:
        cursor.next = stack.pop()
        cursor = cursor.next
    # 将原链表头的下一个结点置为空，否则将成为循环链表
    cursor.next = None
    return sll


def ReverseList(head):
    # write code here
    node = head
    pre = None  # 前一个结点
    while node:
        tin = node  # 记录当前结点
        node = node.next  # 后移
        tin.next = pre  # 将当前结点的next指向前一个结点
        pre = tin  # 更新前一个结点
    return pre  # 返回下一个结点为空的前一个结点，即为新链表头


if __name__ == '__main__':
    sll = SingleLinkList()
    for i in range(10):
        sll.add_rear(i)
    rll = reverse_list(sll)
    print("")
    rll.travel()

    head = ReverseList(rll.head)
    sll2 = SingleLinkList(head)
    sll2.travel()

